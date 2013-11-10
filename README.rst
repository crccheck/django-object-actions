Django Object Actions
=====================

.. image:: https://travis-ci.org/texastribune/django-object-actions.png

If you've ever tried making your own admin object tools and you were
like me, you immediately gave up. Why can't they be as easy as making
Django Admin Actions? Well now they can be.

Similar Packages
~~~~~~~~~~~~~~~~

Django Object Actions is very similar to
`django-object-tools <https://github.com/praekelt/django-object-tools>`_,
but does not require messing with your urls.py, does not do anything
special with permissions, and uses the same patterns as making `admin
actions <https://docs.djangoproject.com/en/dev/ref/contrib/admin/actions/#actions-as-modeladmin-methods>`_
in Django.

Installation
------------

Install Django Object Actions. Currently, this has to be done manually.

Add ``django_object_actions`` to your ``INSTALLED_APPS``.

Alternate Installation
~~~~~~~~~~~~~~~~~~~~~~

Install Django Object Actions. Currently, this has to be done manually.

Copy the templates some place Django's template loader `will find
it <https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs>`_.

Usage
-----

Tools are defined just like defining actions as modeladmin methods, see:
`admin
actions <https://docs.djangoproject.com/en/dev/ref/contrib/admin/actions/#actions-as-modeladmin-methods>`_
for examples and detailed syntax. You can return nothing or an http
response. The major difference being the functions you write will take
an object instance instead of a queryset::

    def toolfunc(self, request, obj)

Tools are exposed by putting them in an ``objectactions`` attribute in
your modeladmin like::

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

Re-using Admin Actions
``````````````````````

If you would like an admin action to also be an object tool, add the
``takes_instance_or_queryset`` decorator like::


    from django_object_actions import DjangoObjectActions
    from django_object_actions.utils import takes_instance_or_queryset


    class RobotAdmin(DjangoObjectActions, admin.ModelAdmin):
        # ... snip ...

        @takes_instance_or_queryset
        def tighten_lug_nuts(self, request, queryset):
            queryset.update(lugnuts=F('lugnuts') - 1)

        objectactions = ['tighten_lug_nuts']
        actions = ['tighten_lug_nuts']


Limitations
~~~~~~~~~~~

django-object-actions expects these functions to be methods of the model
admin.

If you provide your own custom change\_form.html, you'll also need to
manually copy in the relevant bits of `our change
form <https://github.com/texastribune/django-object-actions/blob/master/django_object_actions/templates/django_object_actions/change_form.html>`_.

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
    # start doing stuff
    make test
    make resetdb
    python example_project/manage.py runserver

The fixtures will create a user, admin:admin, you can use to log in
immediately.

Various helpers are available as make commands.
