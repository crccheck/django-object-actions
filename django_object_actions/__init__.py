""" A Django app for adding object tools to models """
__version__ = '0.5.0'


# kind of like __all__, make these available for public
from .utils import (
    BaseDjangoObjectActions,
    DjangoObjectActions,
    takes_instance_or_queryset,
)
