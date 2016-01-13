import mock
from django.test import TestCase

from example_project.polls.models import Poll

from ..utils import (
    BaseDjangoObjectActions,
    takes_instance_or_queryset,
)


class BaseDjangoObjectActionsTest(TestCase):
    def setUp(self):
        self.instance = BaseDjangoObjectActions()

    @mock.patch('django_object_actions.utils.BaseDjangoObjectActions'
                '.admin_site', create=True)
    def test_get_tool_urls_trivial_case(self, mock_site):
        self.instance.model = mock.Mock(
            **{'_meta.app_label': 'app', '_meta.model_name': 'model'})

        urls = self.instance.get_tool_urls([])

        self.assertEqual(len(urls), 1)
        self.assertEqual(urls[0].name, 'app_model_change_tools')

    def test_get_object_actions_gets_attribute(self):
        mock_objectactions = []  # set to something mutable
        mock_request = 'request'
        mock_context = 'context'
        mock_kwargs = {}
        self.instance.objectactions = mock_objectactions
        returned_value = self.instance.get_object_actions(
            mock_request, mock_context, **mock_kwargs
        )
        # assert that `mock_objectactions` was returned
        self.assertEqual(id(mock_objectactions), id(returned_value))
        # WISHLIST assert get_object_actions was called with right args

    def test_get_djoa_button_attrs_returns_defaults(self):
        # TODO: use `mock`
        mock_tool = type('mock_tool', (object, ), {})
        attrs, __ = self.instance.get_djoa_button_attrs(mock_tool)
        self.assertEqual(attrs['class'], '')
        self.assertEqual(attrs['title'], '')

    def test_get_djoa_button_attrs_disallows_href(self):
        mock_tool = type('mock_tool', (object, ), {
            'attrs': {'href': 'hreeeeef'},
        })
        attrs, __ = self.instance.get_djoa_button_attrs(mock_tool)
        self.assertNotIn('href', attrs)

    def test_get_djoa_button_attrs_disallows_title(self):
        mock_tool = type('mock_tool', (object, ), {
            'attrs': {'title': 'i wanna be a title'},
            'short_description': 'real title',
        })
        attrs, __ = self.instance.get_djoa_button_attrs(mock_tool)
        self.assertEqual(attrs['title'], 'real title')

    def test_get_djoa_button_attrs_gets_set(self):
        mock_tool = type('mock_tool', (object, ), {
            'attrs': {'class': 'class'},
            'short_description': 'description',
        })
        attrs, __ = self.instance.get_djoa_button_attrs(mock_tool)
        self.assertEqual(attrs['class'], 'class')
        self.assertEqual(attrs['title'], 'description')

    def test_get_djoa_button_attrs_custom_attrs_get_partitioned(self):
        mock_tool = type('mock_tool', (object, ), {
            'attrs': {'nonstandard': 'wombat'},
        })
        attrs, custom = self.instance.get_djoa_button_attrs(mock_tool)
        self.assertEqual(custom['nonstandard'], 'wombat')


class DecoratorTest(TestCase):
    fixtures = ['sample_data']

    def setUp(self):
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
        # the resulting queryset only has one item and it's self.obj
        self.assertEqual(queryset.get(), self.obj)

        # passing in a queryset yields the same queryset
        queryset = myfunc(None, None, self.queryset)
        self.assertEqual(queryset, self.queryset)

        # passing in an instance yields a queryset (using keyword args)
        queryset = myfunc(None, None, queryset=self.obj)
        # the resulting queryset only has one item and it's self.obj
        self.assertEqual(queryset.get(), self.obj)
