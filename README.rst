Django Object Actions
=====================

.. image:: https://travis-ci.org/texastribune/django-object-actions.png
   :target: https://travis-ci.org/texastribune/django-object-actions

If you've ever tried making your own admin object tools and you were
like me, you immediately gave up. Why can't they be as easy as making
Django Admin Actions? Well now they can be.

Quick-Start Guide
-----------------

Install Django Object Actions::

    pip install django-object-actions

Add ``django_object_actions`` to your ``INSTALLED_APPS``.

In your admin.py::

    from django_object_actions import DjangoObjectActions


    class ArticleAdmin(DjangoObjectActions, admin.ModelAdmin):
        def publish_this(self, request, obj):
            publish_obj(obj)
        publish_this.label = "Publish"  # optional
        publish_this.short_description = "Submit this article to The Texas Tribune"  # optional

        objectactions = ('publish_this', )


Usage
-----

Tools are defined just like defining actions as modeladmin methods, see:
`admin
actions <https://docs.djangoproject.com/en/dev/ref/contrib/admin/actions/#actions-as-modeladmin-methods>`_
for examples and detailed syntax. You can return nothing or an http
response. The major difference being the functions you write will take
an object instance instead of a queryset (see *Re-using Admin Actions* below).

Tools are exposed by putting them in an ``objectactions`` attribute in
your modeladmin like::

    from django_object_actions import DjangoObjectActions


    class MyModelAdmin(DjangoObjectActions, admin.ModelAdmin):
        def toolfunc(self, request, obj):
            pass
        toolfunc.label = "This will be the label of the button"  # optional
        toolfunc.short_description = "This will be the tooltip of the button"  # optional

        objectactions = ('toolfunc', )

Just like actions, you can send a message with ``self.message_user``.
Normally, you would do something to the object and go back to the same
place, but if you return a HttpResponse, it will follow it (hey, just
like actions!).

If your admin modifies ``get_urls``, ``render_change_form``, or
``change_form_template``, you'll need to take extra care.

Re-using Admin Actions
``````````````````````

If you would like an admin action to also be an object tool, add the
``takes_instance_or_queryset`` decorator like::


    from django_object_actions import (DjangoObjectActions,
            takes_instance_or_queryset)


    class RobotAdmin(DjangoObjectActions, admin.ModelAdmin):
        # ... snip ...

        @takes_instance_or_queryset
        def tighten_lug_nuts(self, request, queryset):
            queryset.update(lugnuts=F('lugnuts') - 1)

        objectactions = ['tighten_lug_nuts']
        actions = ['tighten_lug_nuts']

Customizing Admin Actions
`````````````````````````

To give the action some a helpful title tooltip, add a ``short_description``
attribute, similar to how admin actions work::

    def increment_vote(self, request, obj):
        obj.votes = obj.votes + 1
        obj.save()
    increment_vote.short_description = "Increment the vote count by one"

By default, Django Object Actions will guess what to label the button based on
the name of the function. You can override this with a ``label`` attribute::

    def increment_vote(self, request, obj):
        obj.votes = obj.votes + 1
        obj.save()
    increment_vote.label = "Vote++"

If you need even more control, you can add arbitrary attributes to the buttons
by adding a Django widget style `attrs` attribute::

    def increment_vote(self, request, obj):
        obj.votes = obj.votes + 1
        obj.save()
    increment_vote.attrs = {
        'class': 'addlink',
    }


Alternate Installation
``````````````````````

You don't have to add this to ``INSTALLED_APPS``, all you need to to do is copy
the template ``django_object_actions/change_form.html`` some place Django's
template loader `will find it
<https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs>`_.

If you don't intend to use the template customizations at all, don't add
``django_object_actions`` to your ``INSTALLED_APPS`` at all and use
``BaseDjangoObjectActions`` instead of ``DjangoObjectActions``.


Limitations
-----------

1. ``django-object-actions`` expects functions to be methods of the model admin.
   While Django gives you a lot more options for their admin actions.

2. If you provide your own custom ``change_form.html``, you'll also need to
   manually copy in the relevant bits of `our change form
   <https://github.com/texastribune/django-object-actions/blob/master/django_obj
   ect_actions/templates/django_object_actions/change_form.html>`_. You can also
   use ``from django_object_actions import BaseDjangoObjectActions`` instead.

Development
-----------

Getting started *(with virtualenvwrapper)*::

    # get a copy of the code
    git clone git@github.com:texastribune/django-object-actions.git
    cd django-object-actions
    # set up your virtualenv
    mkvirtualenv django-object-actions
    pip install -r requirements-dev.txt
    export DJANGO_SETTINGS_MODULE=example_project.settings
    add2virtualenv .
    make test  # run test suite
    tox  # run full test suite, requires more setup
    make resetdb  # reset the example db
    python example_project/manage.py runserver  # run debug server

The fixtures will create a user, admin:admin, you can use to log in immediately.

Various helpers are available as make commands.


Similar Packages
----------------

Django Object Actions is very similar to
`django-object-tools <https://github.com/praekelt/django-object-tools>`_,
but does not require messing with your urls.py, does not do anything
special with permissions, and uses the same patterns as making `admin
actions <https://docs.djangoproject.com/en/dev/ref/contrib/admin/actions/#actions-as-modeladmin-methods>`_
in Django.

