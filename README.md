Django Object Actions
=====================

If you've ever tried making your own admin object tools and you were like me,
you immediately gave up. Why can't they be as easy as making Django Admin
Actions? Well now they can!

This is very similar to [django-object-tools], but does not require messing with
your urls.py, does not do anything special with permissions, and uses a subset
of the language you already know from making [django admin actions].

  [django-object-tools]: https://github.com/praekelt/django-object-tools
  [django admin actions]: https://docs.djangoproject.com/en/dev/ref/contrib/admin/actions/#actions-as-modeladmin-methods


Installation
------------

Add `django_object_actions` to your `INSTALLED_APPS`.

Or just put the template some place Django can find it.

Example Usage
-------------

Tools are defined just like defining actions as modeladmin methods, see: [django
admin actions] for examples and detailed syntax. The major difference being
the functions you write will take an object instead of a queryset:

    def toolfunc(self, request, obj)

They are exposed by putting them in a `objectactions` attribute in your
modeladmin like:

    class MyModelAdmin(DjangoObjectActions, admin.ModelAdmin):
        def toolfunc(self, request, obj):
            pass
        toolfunc.short_description = "This will be the tooltip of the button"

        objectactions = ('toolfunc',)

Just like actions, you can send a message with `self.message_user`. Normally,
you would do something to the object and go back to the same place, but if you
return a HttpResponse, it will follow it (hey, just like actions!).

Limitations: django-object-actions expects these functions to be methods of the
model admin.

Development
-----------

Getting started:

    pip install -r requirements-dev.txt

Various helpers available as make commands.
