from django.test import TestCase

from example_project.polls.models import Choice


class LoggedInTestCase(TestCase):
    def setUp(self):
        super(LoggedInTestCase, self).setUp()
        self.client.login(username='admin', password='admin')


class AppTests(LoggedInTestCase):
    def test_bare_mixin_works(self):
        # hit admin that doesn't have any tools defined, just the mixin
        response = self.client.get('/admin/polls/poll/add/')
        self.assertEqual(response.status_code, 200)

    def test_configured_mixin_works(self):
        # hit admin that does have any tools defined
        response = self.client.get('/admin/polls/choice/add/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('objectactions', response.context_data)

    def test_tool_func_gets_executed(self):
        c = Choice.objects.get(pk=1)
        votes = c.votes
        response = self.client.get('/admin/polls/choice/1/tools/increment_vote/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response['location'].endswith('/admin/polls/choice/1/'))
        c = Choice.objects.get(pk=1)
        self.assertEqual(c.votes, votes + 1)

    def test_tool_can_return_httpresponse(self):
        # we know this url works because of fixtures
        url = '/admin/polls/choice/2/tools/edit_poll/'
        response = self.client.get(url)
        # we expect a redirect
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response['location'].endswith('/admin/polls/poll/1/'))

    def test_can_return_template(self):
        # This is more of a test of render_to_response than the app, but I think
        # it's good to document that this is something we can do.
        url = '/admin/polls/poll/1/tools/delete_all_choices/'
        response = self.client.get(url)
        self.assertTemplateUsed(response, "clear_choices.html")

    def test_intermediate_page_with_post_works(self):
        self.assertTrue(Choice.objects.filter(poll=1).count())
        url = '/admin/polls/poll/1/tools/delete_all_choices/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Choice.objects.filter(poll=1).count(), 0)
