"""
Integration tests that actually try and use the tools setup in admin.py
"""
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from .tests import LoggedInTestCase
from example_project.polls.factories import CommentFactory, PollFactory


class CommentTest(LoggedInTestCase):
    def test_action_on_a_model_with_uuid_pk_works(self):
        comment = CommentFactory()
        url = '/admin/polls/comment/{0}/tools/hodor/'.format(comment.pk)
        # sanity check that url has a uuid
        self.assertIn('-', url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


class ChangeTest(LoggedInTestCase):
    def test_buttons_load(self):
        url = '/admin/polls/choice/'
        response = self.client.get(url)
        self.assertIn('objectactions', response.context_data)
        self.assertIn('Delete_all', response.rendered_content)

    def test_changelist_action_view(self):
        url = '/admin/polls/choice/tools/delete_all/'
        response = self.client.get(url)
        self.assertRedirects(response, '/admin/polls/choice/')

    def test_changelist_nonexistent_action(self):
        url = '/admin/polls/choice/tools/xyzzy/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_get_changelist_can_remove_action(self):
        poll = PollFactory.create()
        self.assertFalse(poll.question.endswith('?'))
        admin_change_url = reverse('admin:polls_poll_change', args=(poll.pk,))
        action_url = '/admin/polls/poll/1/tools/question_mark/'

        # button is in the admin
        response = self.client.get(admin_change_url)
        self.assertIn(action_url, response.rendered_content)

        response = self.client.get(action_url)  # Click on the button
        self.assertRedirects(response, admin_change_url)

        # button is not in the admin anymore
        response = self.client.get(admin_change_url)
        self.assertNotIn(action_url, response.rendered_content)
