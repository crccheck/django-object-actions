Django Object Actions
=====================

.. image:: https://travis-ci.org/crccheck/django-object-actions.png
   :target: https://travis-ci.org/crccheck/django-object-actions

.. image:: https://coveralls.io/repos/crccheck/django-object-actions/badge.png
    :target: https://coveralls.io/r/crccheck/django-object-actions

If you've ever tried making your own admin object tools and you were
like me, you immediately gave up. Why can't they be as easy as making
Django Admin Actions? Well now they can be.


Quick-Start Guide
-----------------

Install Django Object Actions::

    pip install django-object-actions

Add ``django_object_actions`` to your ``INSTALLED_APPS`` so Django can find our
templates.

In your admin.py::

    from django_object_actions import DjangoObjectActions


    class ArticleAdmin(DjangoObjectActions, admin.ModelAdmin):
        def publish_this(self, request, obj):
            publish_obj(obj)
        publish_this.label = "Publish"  # optional
        publish_this.short_description = "Submit this article"  # optional

        change_actions = ('publish_this', )


Usage
-----

Defining new tool actions are just like defining regular `admin actions
<https://docs.djangoproject.com/en/dev/ref/contrib/admin/actions/>`_. The major
difference is the action functions for you write for the change view will take
an object instance instead of a queryset (see *Re-using Admin Actions* below).

Tool actions are exposed by putting them in a ``change_actions`` attribute in
your model admin. You can also add tool actions to the changelist views too.
You'll get a queryset like a regular admin action::

    from django_object_actions import DjangoObjectActions

    class MyModelAdmin(DjangoObjectActions, admin.ModelAdmin):
        def toolfunc(self, request, obj):
            pass
        toolfunc.label = "This will be the label of the button"  # optional
        toolfunc.short_description = "This will be the tooltip of the button"  # optional

        def make_published(modeladmin, request, queryset):
            queryset.update(status='p')

        change_actions = ('toolfunc', )
        changelist_actions = ('make_published', )

Just like admin actions, you can send a message with ``self.message_user``.
Normally, you would do something to the object and go back to the same
place, but if you return a HttpResponse, it will follow it (hey, just
like admin actions!).

If your admin modifies ``get_urls``, ``change_view``, or ``changelist_view``,
you'll need to take extra care.

Re-using Admin Actions
``````````````````````

If you would like a preexisting admin action to also be an change action, add
the ``takes_instance_or_queryset`` decorator like::


    from django_object_actions import (DjangoObjectActions,
            takes_instance_or_queryset)

    class RobotAdmin(DjangoObjectActions, admin.ModelAdmin):
        # ... snip ...

        @takes_instance_or_queryset
        def tighten_lug_nuts(self, request, queryset):
            queryset.update(lugnuts=F('lugnuts') - 1)

        change_actions = ['tighten_lug_nuts']
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

Programmatically Disabling Actions
``````````````````````````````````

You can programmatically disable registered actions by defining your own custom
``get_change_actions()`` method. In this example, certain actions only apply to
certain object states (i.e. You should not be able to close an company account
if the account is already closed)::

    def get_change_actions(self, request, object_id, form_url):
        actions = super(PollAdmin, self).get_change_actions(request, object_id, form_url)
        actions = list(actions)
        if not request.user.is_superuser:
            return []

        obj = self.model.objects.get(pk=object_id)
        if obj.question.endswith('?'):
            actions.remove('question_mark')

        return actions

The same is true for changelist actions with ``get_changelist_actions``.


Alternate Installation
``````````````````````

You don't have to add this to ``INSTALLED_APPS``, all you need to to do is copy
the template ``django_object_actions/change_form.html`` some place Django's
template loader `will find it
<https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs>`_.

If you don't intend to use the template customizations at all, don't add
``django_object_actions`` to your ``INSTALLED_APPS`` at all and use
``BaseDjangoObjectActions`` instead of ``DjangoObjectActions``.


More Examples
-------------

Making an action that links off-site::

    def external_link(self, request, obj):
        from django.http import HttpResponseRedirect
        url = f'https://example.com/{obj.id}'
        return HttpResponseRedirect(url)


Limitations
-----------

1. ``django-object-actions`` expects functions to be methods of the model admin.
   While Django gives you a lot more options for their admin actions.

2. If you provide your own custom ``change_form.html``, you'll also need to
   manually copy in the relevant bits of `our change form
   <https://github.com/crccheck/django-object-actions/blob/master/django_obj
   ect_actions/templates/django_object_actions/change_form.html>`_. You can also
   use ``from django_object_actions import BaseDjangoObjectActions`` instead.

3. Security. This has been written with the assumption that everyone in the
   Django admin belongs there. Permissions should be enforced in your own
   actions irregardless of what this provides. Better default security is
   planned for the future.


Demo Admin & Docker images
--------------------------

You can try the demo admin against several versions of Django with these Docker
images: https://hub.docker.com/r/crccheck/django-object-actions/

This runs the example Django project in ``./example_project`` based on the
"polls" tutorial. ``admin.py`` demos what you can do with this app.


Development
-----------

Getting started *(with virtualenvwrapper)*::

    # get a copy of the code
    git clone git@github.com:crccheck/django-object-actions.git
    cd django-object-actions
    # set up your virtualenv (with virtualenvwrapper)
    mkvirtualenv django-object-actions
    # Install requirements
    make install
    # Hack your path so that we can reference packages starting from the root
    add2virtualenv .
    make test  # run test suite
    make quickstart  # runs 'make resetdb' and some extra steps

This will install whatever the latest stable version of Django is. You can also
install a specific version of Django and ``pip install -r requirements.txt``.

Various helpers are available as make commands. Type ``make help`` and view the
``Makefile`` to see what other things you can do.


Similar Packages
----------------

If you want an actions menu for each row of your changelist, check out `Django Admin Row Actions
<https://github.com/DjangoAdminHackers/django-admin-row-actions>`_.

Django Object Actions is very similar to
`django-object-tools <https://github.com/praekelt/django-object-tools>`_,
but does not require messing with your urls.py, does not do anything
special with permissions, and uses the same patterns as making `admin
actions <https://docs.djangoproject.com/en/dev/ref/contrib/admin/actions/#actions-as-modeladmin-methods>`_
in Django.
