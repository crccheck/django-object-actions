try:
    from django.contrib.auth import get_user_model
except ImportError:  # pragma: no cover
    # Django 1.4
    from django.contrib.auth.models import User
    get_user_model = lambda: User

import factory


class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = get_user_model()
    first_name = factory.Sequence(lambda i: u'John{0}'.format(i))
    last_name = factory.Sequence(lambda i: u'Doe{0}'.format(i))
    username = factory.LazyAttribute(lambda x: '{0}{1}'.format(
        x.first_name, x.last_name))
    email = factory.LazyAttribute(lambda x: '{0}@{1}.com'.format(
        x.first_name.lower(), x.last_name.lower()))
    password = factory.PostGenerationMethodCall('set_password', 'password')
