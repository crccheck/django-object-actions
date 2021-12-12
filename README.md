Django Object Actions
=====================

[![CI](https://github.com/crccheck/django-object-actions/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/crccheck/django-object-actions/actions/workflows/ci.yml?query=branch%3Amaster)

If you've ever tried making admin object tools you may have thought, "why can't
this be as easy as making Django Admin Actions?" Well now they can be.


Quick-Start Guide
-----------------

Install Django Object Actions:

```shell
$ pip install django-object-actions
```

Add `django_object_actions` to your `INSTALLED_APPS` so Django can find
our templates.

In your admin.py:

```python
from django_object_actions import DjangoObjectActions

class ArticleAdmin(DjangoObjectActions, admin.ModelAdmin):
    def publish_this(self, request, obj):
        publish_obj(obj)
    publish_this.label = "Publish"  # optional
    publish_this.short_description = "Submit this article"  # optional

    change_actions = ('publish_this', )
```


Usage
-----

Defining new &*tool actions* is just like defining regular [admin actions]. The
major difference is the functions for `django-object-actions` will take an
object instance instead of a queryset (see *Re-using Admin Actions* below).

*Tool actions* are exposed by putting them in a `change_actions` attribute in
your `admin.ModelAdmin`. You can also add *tool actions* to the main changelist
views too. There, you'll get a queryset like a regular [admin action][admin actions]:

```python
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
```

Just like admin actions, you can send a message with `self.message_user`.
Normally, you would do something to the object and return to the same url, but
if you return a `HttpResponse`, it will follow it (hey, just like [admin
actions]!).

If your admin modifies `get_urls`, `change_view`, or `changelist_view`,
you'll need to take extra care because `django-object-actions` uses them too.

### Re-using Admin Actions

If you would like a preexisting admin action to also be an *object action*, add
the `takes_instance_or_queryset` decorator to convert object instances into a
queryset and pass querysets:

```python
from django_object_actions import DjangoObjectActions, takes_instance_or_queryset

class RobotAdmin(DjangoObjectActions, admin.ModelAdmin):
    # ... snip ...

    @takes_instance_or_queryset
    def tighten_lug_nuts(self, request, queryset):
        queryset.update(lugnuts=F('lugnuts') - 1)

    change_actions = ['tighten_lug_nuts']
    actions = ['tighten_lug_nuts']
```

[admin actions]: https://docs.djangoproject.com/en/stable/ref/contrib/admin/actions/

### Customizing *Object Actions*

To give the action some a helpful title tooltip, add a
`short_description` attribute, similar to how admin actions work:

```python
def increment_vote(self, request, obj):
    obj.votes = obj.votes + 1
    obj.save()
increment_vote.short_description = "Increment the vote count by one"
```

By default, Django Object Actions will guess what to label the button
based on the name of the function. You can override this with a `label`
attribute:

```python
def increment_vote(self, request, obj):
    obj.votes = obj.votes + 1
    obj.save()
increment_vote.label = "Vote++"
```

If you need even more control, you can add arbitrary attributes to the buttons
by adding a Django widget style
[attrs](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#django.forms.Widget.attrs)
attribute:

```python
def increment_vote(self, request, obj):
    obj.votes = obj.votes + 1
    obj.save()
increment_vote.attrs = {
    'class': 'addlink',
}
```

### Programmatically Disabling Actions

You can programmatically disable registered actions by defining your own
custom `get_change_actions()` method. In this example, certain actions
only apply to certain object states (e.g. You should not be able to
close an company account if the account is already closed):

```python
def get_change_actions(self, request, object_id, form_url):
    actions = super(PollAdmin, self).get_change_actions(request, object_id, form_url)
    actions = list(actions)
    if not request.user.is_superuser:
        return []

    obj = self.model.objects.get(pk=object_id)
    if obj.question.endswith('?'):
        actions.remove('question_mark')

    return actions
```

The same is true for changelist actions with `get_changelist_actions`.

### Alternate Installation

You don't have to add this to `INSTALLED_APPS`, all you need to to do
is copy the template `django_object_actions/change_form.html` some place
Django's template loader [will find
it](https://docs.djangoproject.com/en/stable/ref/settings/#template-dirs).

If you don't intend to use the template customizations at all, don't
add `django_object_actions` to your `INSTALLED_APPS` at all and use
`BaseDjangoObjectActions` instead of `DjangoObjectActions`.


More Examples
-------------

Making an action that links off-site:

```python
def external_link(self, request, obj):
    from django.http import HttpResponseRedirect
    return HttpResponseRedirect(f'https://example.com/{obj.id}')
```


Limitations
-----------

1.  `django-object-actions` expects functions to be methods of the model
    admin. While Django gives you a lot more options for their admin
    actions.
2.  If you provide your own custom `change_form.html`, you'll also need
    to manually copy in the relevant bits of [our change form
    ](./django_object_actions/templates/django_object_actions/change_form.html).
3.  Security. This has been written with the assumption that everyone in
    the Django admin belongs there. Permissions should be enforced in
    your own actions irregardless of what this provides. Better default
    security is planned for the future.


Python and Django compatibility
-------------------------------

See [`ci.yml`](./github/workflows/ci.yml) for which Python and Django versions this supports.


Demo Admin & Docker images
--------------------------

You can try the demo admin against several versions of Django with these Docker
images: https://hub.docker.com/r/crccheck/django-object-actions/tags

This runs the example Django project in `./example_project` based on the "polls"
tutorial. `admin.py` demos what you can do with this app.


Development
-----------

Getting started:

```shell
# get a copy of the code
git clone git@github.com:crccheck/django-object-actions.git
cd django-object-actions
# Install requirements
make install
make test  # run test suite
make quickstart  # runs 'make resetdb' and some extra steps
```

Various helpers are available as make commands. Type `make help` and
view the `Makefile` to see what other things you can do.

Some commands assume you are in the virtualenv. If you see
"ModuleNotFoundError"s, try running `poetry shell` first.


Similar Packages
----------------

If you want an actions menu for each row of your changelist, check out [Django
Admin Row Actions](https://github.com/DjangoAdminHackers/django-admin-row-actions).

Django Object Actions is very similar to
[django-object-tools](https://github.com/praekelt/django-object-tools), but does
not require messing with your urls.py, does not do anything special with
permissions, and uses the same patterns as making [admin actions].
