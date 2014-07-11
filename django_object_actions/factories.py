from django.contrib.auth import get_user_model

import factory


class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = get_user_model()
    first_name = factory.Sequence(lambda i: u'John{}'.format(i))
    last_name = factory.Sequence(lambda i: u'Doe{}'.format(i))
    username = factory.LazyAttribute(lambda x: '{}{}'.format(
        x.first_name, x.last_name))
    email = factory.LazyAttribute(lambda x: '{}@{}.com'.format(
        x.first_name.lower(), x.last_name.lower()))
    password = factory.PostGenerationMethodCall('set_password', 'password')


