<a name="1.1.1"></a>
## [1.1.1](https://github.com/crccheck/django-object-actions/compare/v1.1.0...v1.1.1) (2019-10-06)

### Bug Fixes

* changelist action links had no 'href' (#98) 8b8aed3, closes #96


## 1.1.0

### Added
* [4191afd691] - feat: Make default labels prettier (#93)

### Fixed
* [fb908697a6] - Return to preserved filters on change_list after object action (#88)

## 1.0.0

I didn't get around to everything I listed in #44 as a release blocker for 1.0,
but with Django going 2.0 and dropping backwards compatibility, I decided this
library needs some more stability. In the future look for more removals as
support for older versions of Django keep getting dropped.

https://github.com/crccheck/django-object-actions/compare/v0.10.0...v1.0.0

### Added
* [430be02e59] - Add support for Django 2.0 (#85)

### Changed
* [a7b183f3c1] - Cleanup random Django version support docs (#86)
* [81af3e7cd5] - Add a redirect example to the README (#82)

## 0.10.0

* Add support for Django 1.11 (#76 #78)

https://github.com/crccheck/django-object-actions/compare/v0.9.0...v0.10.0

## 0.9.0

* Add support for all primary key formats (#75)
* Add support for Django 1.10 (#74)
* Documentation tweaks (#71 #70)

### Removed
* Remove support for Django 1.6 (#73)

https://github.com/crccheck/django-object-actions/compare/v0.8.2...v0.9.0

## 0.8.2

* Fix how the demo site stopped working because of bad settings

## 0.8.1

* Fix how extra_context set by admins was not passed
* Fix how if you had multiple admins, you always got redirected to the default admin

## 0.8.0

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
