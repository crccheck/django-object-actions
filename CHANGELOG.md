# Changelog

<!--next-version-placeholder-->

### [3.0.2](https://github.com/crccheck/django-object-actions/compare/v3.0.1...v3.0.2) (2021-04-09)

### Refactors

* Use django.urls.re_path instead of deprecated django.conf.urls.url (#112)

### [3.0.1](https://github.com/crccheck/django-object-actions/compare/v3.0.0...v3.0.1) (2020-08-09)


### Bug Fixes

* Objects with special symbols in primary key 404-ed ([#110](https://github.com/crccheck/django-object-actions/issues/110)) ([0c90ce1](https://github.com/crccheck/django-object-actions/commit/0c90ce12a066baf873037eed415052074430d9d2)), closes [/github.com/django/django/blob/master/django/contrib/admin/utils.py#L17](https://github.com/crccheck//github.com/django/django/blob/master/django/contrib/admin/utils.py/issues/L17)

## [3.0.0](https://github.com/crccheck/django-object-actions/compare/v2.0.0...v3.0.0) (2020-08-08)


### ⚠ BREAKING CHANGES

* **deps:** drop Python 3.4 support in preparation for adding type hints and Django 3.1 support

### Features

* **deps:** Add Django 3.1 support ([#109](https://github.com/crccheck/django-object-actions/issues/109)) ([2c7170e](https://github.com/crccheck/django-object-actions/commit/2c7170e3a73317a9417733a7ddfe0fabab84fe85))
* **deps:** Drop Python 3.4 support ([#108](https://github.com/crccheck/django-object-actions/issues/108)) ([68519d4](https://github.com/crccheck/django-object-actions/commit/68519d48fa8dd4d3b203981a52157841e5152774)), closes [#107](https://github.com/crccheck/django-object-actions/issues/107)
* add Django 3 test support ([#106](https://github.com/crccheck/django-object-actions/issues/106)) ([4eaf14c](https://github.com/crccheck/django-object-actions/commit/4eaf14c3caff36d5ab274835d38baef7e66213dc))

## [2.0.0](https://github.com/crccheck/django-object-actions/compare/v1.1.2...v2.0.0) (2019-11-30)


### ⚠ BREAKING CHANGES

* This release drops Python 2 support

Django has [dropped Python 2 support](https://docs.djangoproject.com/en/2.2/releases/2.0/#python-compatibility) ever since Django 2.0 (December 2, 2017). With Django 3.0 coming very soon and Python 2 reaching end of life, it doesn't make sense to continue supporting Python 2.

### Features

* Drop Python 2 support ([#105](https://github.com/crccheck/django-object-actions/issues/105)) ([551d2bb](https://github.com/crccheck/django-object-actions/commit/551d2bb2a66c5fd1c157b05c288032124affba41))

### [1.1.2](https://github.com/crccheck/django-object-actions/compare/v1.1.1...v1.1.2) (2019-11-14)

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
