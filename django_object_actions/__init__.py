"""A Django app for adding object tools for models in the admin."""
__version__ = "3.0.1"


# kind of like __all__, make these available for public
from .utils import (
    BaseDjangoObjectActions,
    DjangoObjectActions,
    takes_instance_or_queryset,
)
