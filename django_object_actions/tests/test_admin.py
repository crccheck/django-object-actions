"""
Integration tests that actually try and use the tools setup in admin.py
"""
from __future__ import unicode_literals

from .tests import LoggedInTestCase
from example_project.polls.factories import CommentFactory


class CommentTest(LoggedInTestCase):
    def test_action_on_a_model_with_uuid_pk_works(self):
        comment = CommentFactory()
        url = '/admin/polls/comment/{0}/tools/hodor/'.format(comment.pk)
        # sanity check that url has a uuid
        self.assertIn('-', url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
