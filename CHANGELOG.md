0.8.0 (unreleased)
------------------

### Breaking changes

* Deleted `get_objectactions(request, context, **kwargs)`. If you used this
  before, use `get_change_actions(request, object_id, form_url)` instead. To
  get at the original object, instead of `context['original']`, you can use
  `self.model.get(pk=object_id)`, `self.get_object(request, object_id)`, etc.
  This isn't as convenient as it used to be, but now it uses the officially
  documented way to add extra context to admin views.
  https://docs.djangoproject.com/en/dev/ref/contrib/admin/#other-methods

* Renamed `objectactions`. In your admin, instead of defining your actions in
  the `objectactions` attribute, use `change_actions`.
