# Changelog

<!--next-version-placeholder-->
### Feature
* Drop support for GET method. All action are now invoked with POST method.
* Add option to include inline forms with actions.

### Breaking
* When dealing with a secondary form in action, you cannot simply check the http method to determine if the form should be rendered or processed. You need to check for specific form inputs in POST payload.

## v4.1.0 (2022-11-14)
### Feature
* Provide action decorator to pass label, description and atts to the admin method ([#141](https://github.com/crccheck/django-object-actions/issues/141)) ([`5638f99`](https://github.com/crccheck/django-object-actions/commit/5638f999d32ea7f6de60b895d23ce89624120769))

### Fix
* Fix link to ci.yml in README ([#139](https://github.com/crccheck/django-object-actions/issues/139)) ([`700dd9b`](https://github.com/crccheck/django-object-actions/commit/700dd9b848aea67c759dca61cd815a27b6b16fd1))

## v4.0.0 (2022-03-12)
### Feature
* Drop Python 3.6 support ([#135](https://github.com/crccheck/django-object-actions/issues/135)) ([`8deebed`](https://github.com/crccheck/django-object-actions/commit/8deebedda55d0e5d466969c7f27a9c60e680e5e8))

### Fix
* Cleanup Django compatibility shims for <2.0 ([#126](https://github.com/crccheck/django-object-actions/issues/126)) ([`88cfb3b`](https://github.com/crccheck/django-object-actions/commit/88cfb3b2e06b17762639da7f48259eeae343942f))

### Breaking
* Python 3.6 is past end-of-life and is no longer supported. Keeping it in `pyproject.toml` was causing pains trying to install packages. Let's drop it while we're dropping support for other old stuff. ([`8deebed`](https://github.com/crccheck/django-object-actions/commit/8deebedda55d0e5d466969c7f27a9c60e680e5e8))

### Documentation
* Add Django@4.0 to CI ([#133](https://github.com/crccheck/django-object-actions/issues/133)) ([`20e2418`](https://github.com/crccheck/django-object-actions/commit/20e2418e6ada4651b3e6d51b5d10c545d8a6c863))

## v3.1.0 (2021-12-18)
### Feature
* **ci:** Add manual semantic-release ([#128](https://github.com/crccheck/django-object-actions/issues/128)) ([`f43fd11`](https://github.com/crccheck/django-object-actions/commit/f43fd1199a72be013766d437fe54d875e2fdd53f))
* Add Python 3.9 & 3.10 support ([`28f0ef7`](https://github.com/crccheck/django-object-actions/commit/28f0ef7dd62eedbdac9d34ad115245ef8d935c4d))

### Fix
* Fix typo in version_variable ([#130](https://github.com/crccheck/django-object-actions/issues/130)) ([`040a802`](https://github.com/crccheck/django-object-actions/commit/040a8029c298d8bb17ffab0b75b9b9ecc3d70de2))

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
