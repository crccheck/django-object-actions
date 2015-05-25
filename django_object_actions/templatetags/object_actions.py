# -*- encoding: utf8 -*-
import re
from django.template import Library


register = Library()

@register.inclusion_tag('django_object_actions/object_actions.html', takes_context=True)
def object_actions(context):
    return {
        'objectactions': context['objectactions'],
    }

