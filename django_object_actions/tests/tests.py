from django.urls import reverse
from django.test import TestCase

from example_project.polls.factories import UserFactory
from example_project.polls.models import Choice


class LoggedInTestCase(TestCase):
    def setUp(self):
        super(LoggedInTestCase, self).setUp()
        UserFactory.create(
            is_staff=True, is_superuser=True, username="admin", password="admin"
        )
        self.assertTrue(self.client.login(username="admin", password="admin"))


# TODO move most of these to test_admin.py after I sit down and re-read these
# and don't need the fixtures
class AppTests(LoggedInTestCase):
    fixtures = ["sample_data"]

    def test_tool_func_gets_executed(self):
        c = Choice.objects.get(pk=1)
        votes = c.votes
        response = self.client.get(
            reverse("admin:polls_choice_actions", args=(1, "increment_vote"))
        )
        self.assertEqual(response.status_code, 302)
        url = reverse("admin:polls_choice_change", args=(1,))
        self.assertTrue(response["location"].endswith(url))
        c = Choice.objects.get(pk=1)
        self.assertEqual(c.votes, votes + 1)

    def test_tool_can_return_httpresponse(self):
        # we know this url works because of fixtures
        url = reverse("admin:polls_choice_actions", args=(2, "edit_poll"))
        response = self.client.get(url)
        # we expect a redirect
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            response["location"].endswith(reverse("admin:polls_poll_change", args=(1,)))
        )

    def test_can_return_template(self):
        # This is more of a test of render_to_response than the app, but I think
        # it's good to document that this is something we can do.
        url = reverse("admin:polls_poll_actions", args=(1, "delete_all_choices"))
        response = self.client.get(url)
        self.assertTemplateUsed(response, "clear_choices.html")

    def test_message_user_sends_message(self):
        url = reverse("admin:polls_poll_actions", args=(1, "delete_all_choices"))
        self.assertNotIn("messages", self.client.cookies)
        self.client.get(url)
        self.assertIn("messages", self.client.cookies)

    def test_intermediate_page_with_post_works(self):
        self.assertTrue(Choice.objects.filter(poll=1).count())
        url = reverse("admin:polls_poll_actions", args=(1, "delete_all_choices"))
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Choice.objects.filter(poll=1).count(), 0)

    def test_undefined_tool_404s(self):
        response = self.client.get(
            reverse("admin:polls_poll_actions", args=(1, "weeeewoooooo"))
        )
        self.assertEqual(response.status_code, 404)

    def test_key_error_tool_500s(self):
        self.assertRaises(
            KeyError,
            self.client.get,
            reverse("admin:polls_choice_actions", args=(1, "raise_key_error")),
        )

    def test_render_button(self):
        response = self.client.get(reverse("admin:polls_choice_change", args=(1,)))
        self.assertEqual(response.status_code, 200)
