import factory
from django.contrib.auth import get_user_model
from django.utils import timezone
from factory import faker

from . import models


fake = faker.faker.Factory.create()


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_user_model()
    first_name = factory.LazyAttribute(lambda i: fake.first_name())
    last_name = factory.LazyAttribute(lambda i: fake.last_name())
    username = factory.LazyAttribute(lambda x: '{0}{1}'.format(x.first_name, x.last_name))
    email = factory.LazyAttribute(lambda x: '{0}@{1}.com'.format(
        x.first_name.lower(), x.last_name.lower()))
    password = factory.PostGenerationMethodCall('set_password', 'password')


class PollFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Poll

    question = factory.LazyAttribute(lambda __: fake.sentence())
    pub_date = factory.LazyAttribute(lambda __: timezone.now())


class ChoiceFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Choice

    poll = factory.SubFactory(PollFactory)
    choice_text = factory.LazyAttribute(lambda __: fake.word())
    votes = factory.LazyAttribute(lambda __: fake.pyint())


class CommentFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Comment
