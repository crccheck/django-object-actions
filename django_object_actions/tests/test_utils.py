from django.test import TestCase

from example_project.polls.models import Poll

from ..utils import QuerySetIsh


class QuerySetIshTest(TestCase):
    def setUp(self):
        # as defined in initial_data fixture
        # WISHLIST don't depend on fixture
        self.obj = Poll.objects.get(pk=1)

    def test_can_turn_object_into_queryset(self):
        qs = QuerySetIsh(self.obj)
        self.assertEqual(qs.count(), 1)
        self.assertEqual(qs.get(), self.obj)
        self.assertEqual(qs.order_by('foo').get(), self.obj)
        self.assertEqual(qs.all().get(), self.obj)
        self.assertEqual(qs.filter().get(), self.obj)
        self.assertEqual(qs.latest('bar'), self.obj)
