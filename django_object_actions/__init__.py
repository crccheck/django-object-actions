"""A Django app for adding object tools for models in the admin."""

__version__ = "4.3.0"


from .utils import (
    BaseDjangoObjectActions,
    DjangoObjectActions,
    action,
    takes_instance_or_queryset,
)

__all__ = [
    "BaseDjangoObjectActions",
    "DjangoObjectActions",
    "action",
    "takes_instance_or_queryset",
]
