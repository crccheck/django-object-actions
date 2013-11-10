from django.db.models.query import QuerySet
from django.test import TestCase

from example_project.polls.models import Poll

from ..utils import QuerySetIsh, takes_instance_or_queryset


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


class DecoratorTest(TestCase):
    def setUp(self):
        # as defined in initial_data fixture
        # WISHLIST don't depend on fixture
        self.obj = Poll.objects.get(pk=1)
        self.queryset = Poll.objects.all()

    def test_trivial(self):
        # setup
        def myfunc(foo, bar, queryset):
            return queryset

        # make sure my test function outputs the third arg
        self.assertEqual(myfunc(None, None, 'foo'), 'foo')
        # or the `queryset` kwarg
        self.assertEqual(myfunc(None, None, queryset='bar'), 'bar')

    def test_decorated(self):
        # setup
        @takes_instance_or_queryset
        def myfunc(foo, bar, queryset):
            return queryset

        # passing in an instance yields a queryset (using positional args)
        queryset = myfunc(None, None, self.obj)
        self.assertIsInstance(queryset, QuerySet)
        # the resulting queryset only has one item and it's self.obj
        self.assertEqual(queryset.get(), self.obj)

        # passing in a queryset yields the same queryset
        queryset = myfunc(None, None, self.queryset)
        self.assertIsInstance(queryset, QuerySet)
        self.assertEqual(queryset, self.queryset)

        # passing in an instance yields a queryset (using keyword args)
        queryset = myfunc(None, None, queryset=self.obj)
        self.assertIsInstance(queryset, QuerySet)
        # the resulting queryset only has one item and it's self.obj
        self.assertEqual(queryset.get(), self.obj)
