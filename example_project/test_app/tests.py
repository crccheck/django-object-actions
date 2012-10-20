from django.test import TestCase


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
