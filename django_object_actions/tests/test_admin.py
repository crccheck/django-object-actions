"""
Integration tests that actually try and use the tools setup in admin.py
"""
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from .tests import LoggedInTestCase
from example_project.polls.factories import CommentFactory, PollFactory


class CommentTests(LoggedInTestCase):
    def test_action_on_a_model_with_uuid_pk_works(self):
        comment = CommentFactory()
        url = '/admin/polls/comment/{0}/actions/hodor/'.format(comment.pk)
        # sanity check that url has a uuid
        self.assertIn('-', url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


class ChangeTests(LoggedInTestCase):
    def test_buttons_load(self):
        url = '/admin/polls/choice/'
        response = self.client.get(url)
        self.assertIn('objectactions', response.context_data)
        self.assertIn('Delete_all', response.rendered_content)

    def test_changelist_template_context(self):
        url = reverse('admin:polls_poll_changelist')
        response = self.client.get(url)
        self.assertIn('objectactions', response.context_data)
        self.assertIn('tools_view_name', response.context_data)
        self.assertIn('foo', response.context_data)

    def test_changelist_action_view(self):
        url = '/admin/polls/choice/actions/delete_all/'
        response = self.client.get(url)
        self.assertRedirects(response, '/admin/polls/choice/')

    def test_changelist_nonexistent_action(self):
        url = '/admin/polls/choice/actions/xyzzy/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_get_changelist_can_remove_action(self):
        poll = PollFactory.create()
        self.assertFalse(poll.question.endswith('?'))
        admin_change_url = reverse('admin:polls_poll_change', args=(poll.pk,))
        action_url = '/admin/polls/poll/1/actions/question_mark/'

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
        url = reverse('admin:polls_poll_change', args=(poll.pk,))

        response = self.client.get(url)
        self.assertIn('objectactions', response.context_data)
        self.assertIn('tools_view_name', response.context_data)
        self.assertIn('foo', response.context_data)
