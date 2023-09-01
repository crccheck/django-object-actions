"""
Integration tests that actually try and use the tools setup in admin.py
"""
from django.contrib.admin.utils import quote
from django.http import HttpResponse
from django.urls import reverse
from unittest.mock import patch

from .tests import LoggedInTestCase
from example_project.polls.factories import (
    ChoiceFactory,
    CommentFactory,
    PollFactory,
    RelatedDataFactory,
)


class CommentTests(LoggedInTestCase):
    def test_action_on_a_model_with_uuid_pk_works(self):
        comment = CommentFactory()
        comment_url = reverse("admin:polls_comment_change", args=(comment.pk,))
        action_url = "/admin/polls/comment/{0}/actions/hodor/".format(comment.pk)
        # sanity check that url has a uuid
        self.assertIn("-", action_url)
        response = self.client.post(action_url)
        self.assertRedirects(response, comment_url)

    @patch("django_object_actions.utils.ChangeActionView.post")
    def test_action_on_a_model_with_arbitrary_pk_works(self, mock_view):
        mock_view.return_value = HttpResponse()
        action_url = "/admin/polls/comment/{0}/actions/hodor/".format(" i am a pk ")

        self.client.post(action_url)

        self.assertTrue(mock_view.called)
        self.assertEqual(mock_view.call_args[1]["pk"], " i am a pk ")

    @patch("django_object_actions.utils.ChangeActionView.post")
    def test_action_on_a_model_with_slash_in_pk_works(self, mock_view):
        mock_view.return_value = HttpResponse()
        action_url = "/admin/polls/comment/{0}/actions/hodor/".format("pk/slash")

        self.client.post(action_url)

        self.assertTrue(mock_view.called)
        self.assertEqual(mock_view.call_args[1]["pk"], "pk/slash")


class ExtraTests(LoggedInTestCase):
    def test_action_on_a_model_with_complex_id(self):
        related_data = RelatedDataFactory()
        related_data_url = reverse(
            "admin:polls_relateddata_change", args=(related_data.pk,)
        )
        action_url = "/admin/polls/relateddata/{}/actions/fill_up/".format(
            quote(related_data.pk)
        )

        response = self.client.post(action_url)
        self.assertNotEqual(response.status_code, 404)
        self.assertRedirects(response, related_data_url)


class ChangeTests(LoggedInTestCase):
    def test_buttons_load(self):
        url = "/admin/polls/choice/"
        response = self.client.get(url)
        self.assertIn("objectactions", response.context_data)
        self.assertIn("Delete all", response.rendered_content)

    def test_changelist_template_context(self):
        url = reverse("admin:polls_poll_changelist")
        response = self.client.get(url)
        self.assertIn("objectactions", response.context_data)
        self.assertIn("tools_view_name", response.context_data)
        self.assertIn("foo", response.context_data)

    def test_changelist_action_view(self):
        url = "/admin/polls/choice/actions/delete_all/"
        response = self.client.post(url)
        self.assertRedirects(response, "/admin/polls/choice/")

    def test_changelist_nonexistent_action(self):
        url = "/admin/polls/choice/actions/xyzzy/"
        response = self.client.post(url)
        self.assertEqual(response.status_code, 404)

    def test_get_changelist_can_remove_action(self):
        poll = PollFactory.create()
        self.assertFalse(poll.question.endswith("?"))
        admin_change_url = reverse("admin:polls_poll_change", args=(poll.pk,))
        action_url = "/admin/polls/poll/1/actions/question_mark/"

        # button is in the admin
        response = self.client.get(admin_change_url)
        self.assertIn(action_url, response.rendered_content)

        response = self.client.post(action_url)  # Click on the button
        self.assertRedirects(response, admin_change_url)

        # button is not in the admin anymore
        response = self.client.get(admin_change_url)
        self.assertNotIn(action_url, response.rendered_content)

    def test_changelist_get_method_action_view(self):
        url = "/admin/polls/choice/actions/delete_all/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 405)

    def test_changelist_get_method_nonexistent_action(self):
        url = "/admin/polls/choice/actions/xyzzy/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 405)


class ChangeListTests(LoggedInTestCase):
    def test_changelist_template_context(self):
        poll = PollFactory()
        url = reverse("admin:polls_poll_change", args=(poll.pk,))

        response = self.client.get(url)
        self.assertIn("objectactions", response.context_data)
        self.assertIn("tools_view_name", response.context_data)
        self.assertIn("foo", response.context_data)


class MultipleAdminsTests(LoggedInTestCase):
    def test_redirect_back_from_secondary_admin(self):
        poll = PollFactory()
        admin_change_url = reverse(
            "admin:polls_poll_change", args=(poll.pk,), current_app="support"
        )
        action_url = "/support/polls/poll/1/actions/question_mark/"
        self.assertTrue(admin_change_url.startswith("/support/"))

        response = self.client.post(action_url)
        self.assertRedirects(response, admin_change_url)


class FormTests(LoggedInTestCase):
    def test_form_is_rendered_in_change_view(self):
        choice = ChoiceFactory()
        admin_change_url = reverse("admin:polls_choice_change", args=(choice.pk,))

        response = self.client.get(admin_change_url)

        # form is in the admin
        action_url_lookup = 'action="/admin/polls/choice/1/actions/change_votes/"'
        self.assertIn(action_url_lookup, response.rendered_content)
        form_lookup = '<form name="change_votes__form"'
        self.assertIn(form_lookup, response.rendered_content)

        # form has input
        input_lookup = 'name="change_by"'
        self.assertIn(input_lookup, response.rendered_content)

    def test_form_is_rendered_in_changelist(self):
        admin_change_url = reverse("admin:polls_choice_changelist")

        response = self.client.get(admin_change_url)

        # form is in the admin
        action_url_lookup = 'action="/admin/polls/choice/actions/reset_all/"'
        self.assertIn(action_url_lookup, response.rendered_content)
        form_lookup = '<form name="reset_all__form"'
        self.assertIn(form_lookup, response.rendered_content)

        # form has input
        input_lookup = 'name="new_value"'
        self.assertIn(input_lookup, response.rendered_content)
