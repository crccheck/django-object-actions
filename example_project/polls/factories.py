import factory

from . import models


class CommentFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Comment
