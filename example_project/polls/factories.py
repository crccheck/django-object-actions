import factory
from django.contrib.auth import get_user_model
from django.utils import timezone

from . import models


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.Faker("slug")
    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "password")


class PollFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Poll

    question = factory.Faker("sentence")
    pub_date = factory.LazyAttribute(lambda __: timezone.now())


class ChoiceFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Choice

    poll = factory.SubFactory(PollFactory)
    choice_text = factory.Faker("word")
    votes = factory.Faker("pyint")


class CommentFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Comment
