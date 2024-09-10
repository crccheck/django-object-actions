import random
import string

import factory
from django.contrib.auth import get_user_model
from django.utils import timezone

from . import models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.Faker("slug")
    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "password")


class PollFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Poll

    question = factory.Faker("sentence")
    pub_date = factory.LazyAttribute(lambda __: timezone.now())


class ChoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Choice

    poll = factory.SubFactory(PollFactory)
    choice_text = factory.Faker("word")
    votes = factory.Faker("pyint")


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Comment


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str


class RelatedDataFactory(factory.django.DjangoModelFactory):
    id = factory.lazy_attribute(
        lambda __: f"{get_random_string(2)}:{get_random_string(2)}-{get_random_string(2)}!{get_random_string(2)}"
    )

    class Meta:
        model = models.RelatedData
