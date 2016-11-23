0.8.2
-----

* Fix how the demo site stopped working because of bad settings

0.8.1
-----

* Fix how extra_context set by admins was not passed
* Fix how if you had multiple admins, you always got redirected to the default admin

0.8.0
-----

* Renames `objectactions` to `change_actions`
* Removes `get_object_actions` (see below)
* Adds `changelist_actions` for creating action tools in the change list view too
* Adds `get_change_actions` and `get_changelist_actions`

### Breaking changes

* Deleted `get_object_actions(request, context, **kwargs)`. If you used this
  before, use `get_change_actions(request, object_id, form_url)` instead. To
  get at the original object, instead of `context['original']`, you can use
  `self.model.get(pk=object_id)`, `self.get_object(request, object_id)`, etc.
  This isn't as convenient as it used to be, but now it uses the officially
  documented way to add extra context to admin views.
  https://docs.djangoproject.com/en/dev/ref/contrib/admin/#other-methods

* Renamed `objectactions`. In your admin, instead of defining your actions in
  the `objectactions` attribute, use `change_actions`.
