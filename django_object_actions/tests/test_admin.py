"""
Integration tests that actually try and use the tools setup in admin.py
"""

from unittest.mock import patch

from django.contrib.admin.utils import quote
from django.http import HttpResponse
from django.urls import reverse

from example_project.polls.admin import RelatedDataAdmin
from example_project.polls.factories import (
    CommentFactory,
    PollFactory,
    RelatedDataFactory,
)
from example_project.polls.models import RelatedData

from .tests import LoggedInTestCase


class Issue137Tests(LoggedInTestCase):
    """Test that object_id passed to get_change_actions is unquoted (issue #137)."""

    def test_get_change_actions_can_query_with_object_id(self):
        """
        When a model has a CharField primary key with characters that get
        quoted in URLs (like underscores), get_change_actions should receive
        the unquoted value so it can query the database, matching Django admin's
        behavior.
        """
        from django.contrib import admin as django_admin

        related_data = RelatedDataFactory(id="user_001_name")

        class QueryingAdmin(RelatedDataAdmin):
            def get_change_actions(self, request, object_id, form_url):
                # Before fix, this would fail because object_id is still quoted
                obj = self.model.objects.get(pk=object_id)
                if obj.id == related_data.id:
                    return ["fill_up"]
                return []

        django_admin.site.unregister(RelatedData)
        django_admin.site.register(RelatedData, QueryingAdmin)
        try:
            admin_change_url = reverse(
                "admin:polls_relateddata_change", args=(related_data.pk,)
            )
            response = self.client.get(admin_change_url)
            self.assertEqual(response.status_code, 200)
            # Action should be present since we returned it
            self.assertIn("fill_up", response.rendered_content)
        finally:
            django_admin.site.unregister(RelatedData)
            django_admin.site.register(RelatedData, RelatedDataAdmin)

    def test_change_view_with_quoted_pk_renders_correct_actions(self):
        """
        If get_change_actions uses the object_id to look up the model
        (e.g. self.model.objects.get(pk=object_id)), it must work with
        CharField pks that contain URL-quoteable characters.
        """
        related_data = RelatedDataFactory(id="item_001_test")
        quoted_pk = quote(related_data.pk)
        self.assertNotEqual(quoted_pk, related_data.pk)

        admin_change_url = reverse(
            "admin:polls_relateddata_change", args=(related_data.pk,)
        )
        response = self.client.get(admin_change_url)
        self.assertEqual(response.status_code, 200)
        # The action button for 'fill_up' should be rendered
        self.assertIn("fill_up", response.rendered_content)


class CommentTests(LoggedInTestCase):
    def test_action_on_a_model_with_uuid_pk_works(self):
        comment = CommentFactory()
        comment_url = reverse("admin:polls_comment_change", args=(comment.pk,))
        action_url = f"/admin/polls/comment/{comment.pk}/actions/hodor/"
        # sanity check that url has a uuid
        self.assertIn("-", action_url)
        response = self.client.get(action_url)
        self.assertRedirects(response, comment_url)

    @patch("django_object_actions.utils.ChangeActionView.dispatch")
    def test_action_on_a_model_with_arbitrary_pk_works(self, mock_view):
        mock_view.return_value = HttpResponse()
        action_url = "/admin/polls/comment/{}/actions/hodor/".format(" i am a pk ")

        self.client.get(action_url)

        self.assertTrue(mock_view.called)
        self.assertEqual(mock_view.call_args[1]["pk"], " i am a pk ")

    @patch("django_object_actions.utils.ChangeActionView.dispatch")
    def test_action_on_a_model_with_slash_in_pk_works(self, mock_view):
        mock_view.return_value = HttpResponse()
        action_url = "/admin/polls/comment/{}/actions/hodor/".format("pk/slash")

        self.client.get(action_url)

        self.assertTrue(mock_view.called)
        self.assertEqual(mock_view.call_args[1]["pk"], "pk/slash")


class ExtraTests(LoggedInTestCase):
    def test_action_on_a_model_with_complex_id(self):
        related_data = RelatedDataFactory()
        related_data_url = reverse(
            "admin:polls_relateddata_change", args=(related_data.pk,)
        )
        action_url = (
            f"/admin/polls/relateddata/{quote(related_data.pk)}/actions/fill_up/"
        )

        response = self.client.get(action_url)
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
        url = reverse("admin:polls_choice_actions", args=("delete_all",))
        response = self.client.get(url)
        self.assertRedirects(response, "/admin/polls/choice/")

    def test_changelist_action_post_only_tool_rejects_get(self):
        poll = PollFactory.create()
        url = reverse("admin:polls_choice_actions", args=(poll.pk, "reset_vote"))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 405)

    def test_changelist_nonexistent_action(self):
        url = "/admin/polls/choice/actions/xyzzy/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_get_changelist_can_remove_action(self):
        poll = PollFactory.create()
        self.assertFalse(poll.question.endswith("?"))
        admin_change_url = reverse("admin:polls_poll_change", args=(poll.pk,))
        action_url = "/admin/polls/poll/1/actions/question_mark/"

        # button is in the admin
        response = self.client.get(admin_change_url)
        self.assertIn(action_url, response.rendered_content)

        response = self.client.get(action_url)  # Click on the button
        self.assertRedirects(response, admin_change_url)

        # button is not in the admin anymore
        response = self.client.get(admin_change_url)
        self.assertNotIn(action_url, response.rendered_content)


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

        response = self.client.get(action_url)
        self.assertRedirects(response, admin_change_url)
