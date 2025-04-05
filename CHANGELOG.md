# CHANGELOG


## v5.0.0 (2025-04-05)

### Bug Fixes

- **ci**: Fix release should use python-semantic-release/publish-action
  ([#183](https://github.com/crccheck/django-object-actions/pull/183),
  [`ce75176`](https://github.com/crccheck/django-object-actions/commit/ce75176329fda9e9776a77525bf98d55c0a4150f))

Unable to resolve action `python-semantic-release/upload-to-gh-release@9.21.0`, unable to find
  version `9.21.0`

It is now named `python-semantic-release/publish-action`

- **ci**: Fix renamed branch s/master/main
  ([#184](https://github.com/crccheck/django-object-actions/pull/184),
  [`6e1a451`](https://github.com/crccheck/django-object-actions/commit/6e1a451cbf4e5818c10d637856884b1c88b4c4f3))

- **ci**: Typo in publish-action tag
  ([#185](https://github.com/crccheck/django-object-actions/pull/185),
  [`0228a99`](https://github.com/crccheck/django-object-actions/commit/0228a996dfaaa8bf56276f76e8cd8af5ce387272))

### Chores

- Add Ruff and use it for lint checks
  ([#175](https://github.com/crccheck/django-object-actions/pull/175),
  [`8478467`](https://github.com/crccheck/django-object-actions/commit/847846774442f20ac4ffc68f7f1f53707f53b209))

- Drop long-unsupported py3.7 py3.8 django versions
  ([#179](https://github.com/crccheck/django-object-actions/pull/179),
  [`988ce82`](https://github.com/crccheck/django-object-actions/commit/988ce82b39e92fa282ac0201cd105093b2d11289))

Python 3.7 hasn't been supported in ages, and it's causing errors on CI actions so let's just drop
  it.

It appears that [dropping Python 3.7 is desired
  anyway](https://github.com/crccheck/django-object-actions/blob/master/CHANGELOG.md#v430-2024-09-10)!

- Run tests for Django 5.1 on tested Python versions
  ([#178](https://github.com/crccheck/django-object-actions/pull/178),
  [`6e92eb7`](https://github.com/crccheck/django-object-actions/commit/6e92eb739969c63b0a4bcd1e7f134f14a8517d1f))

- Switch from Poetry to vanilla Pip
  ([#180](https://github.com/crccheck/django-object-actions/pull/180),
  [`080ee8c`](https://github.com/crccheck/django-object-actions/commit/080ee8c88e19282bbf147a8a4a4c6091374150a0))

Updating the project to match my current style and to reduce dependencies.

- **ci**: Add Django 5.2 to test matrix
  ([#182](https://github.com/crccheck/django-object-actions/pull/182),
  [`a89ca4f`](https://github.com/crccheck/django-object-actions/commit/a89ca4f207cd668c21834f3370bb62e87fe65195))

No code changes needed for Django 5.2 support

https://docs.djangoproject.com/en/5.2/releases/5.2/

### Refactoring

- Add more lint rules ([#181](https://github.com/crccheck/django-object-actions/pull/181),
  [`fa2b4d7`](https://github.com/crccheck/django-object-actions/commit/fa2b4d720662337fe9b7217661bf984f11640229))

Bringing in rules I've had success with elsewhere. More consistent style helps with readability and
  maintainability. Some of the rules help with code simplicity and with reducing bugs too.


## v4.3.0 (2024-09-10)

### Chores

- Add Django v5 to CI matrix ([#166](https://github.com/crccheck/django-object-actions/pull/166),
  [`b63aac1`](https://github.com/crccheck/django-object-actions/commit/b63aac1e919c986df9687699c6494dab3093b295))

https://docs.djangoproject.com/en/5.0/releases/5.0/

- Update Django/Python test matrix and add classifier for py3.12
  ([#171](https://github.com/crccheck/django-object-actions/pull/171),
  [`ad3b898`](https://github.com/crccheck/django-object-actions/commit/ad3b8987c5b20391c3e5b56147c799e9aa4804bd))

- **ci**: Upgrade python-semantic-release to v9.8.8
  ([#176](https://github.com/crccheck/django-object-actions/pull/176),
  [`50a03af`](https://github.com/crccheck/django-object-actions/commit/50a03afdf1571a5cb17db282df089f81a3c20ad2))

There have been a lot of releases since v8.0.8
  https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md#v808-2023-08-26

The breaking change was dropping Python 3.7. While this project supports 3.7... that will change the
  next opportunity

### Code Style

- Apply Black formatting ([#170](https://github.com/crccheck/django-object-actions/pull/170),
  [`fb3ce5b`](https://github.com/crccheck/django-object-actions/commit/fb3ce5b75bda44dfd3185c25e9cf7e943ca6fb61))

### Documentation

- Add Django Modal Actions as a similar package
  ([#173](https://github.com/crccheck/django-object-actions/pull/173),
  [`813687e`](https://github.com/crccheck/django-object-actions/commit/813687e76241f8a6786fa20ea707ae470f1463ab))

Adding new Django Modal Actions package Deleting Django Object Actions which hasn't had a commit in
  3 years

### Features

- Add a way to make a POST only action
  ([#174](https://github.com/crccheck/django-object-actions/pull/174),
  [`494d581`](https://github.com/crccheck/django-object-actions/commit/494d5817307343018ccc8398d64f95228e57f51b))

Followup to #168 to get CI to pass again, documents how to make a POST only action, and adds some
  test coverage.

There are still a few cleanup issues but this should get things moving on POST only actions again.


## v4.2.0 (2023-09-08)

### Bug Fixes

- **ci**: Maybe this will fix Semantic Release
  ([#161](https://github.com/crccheck/django-object-actions/pull/161),
  [`1595348`](https://github.com/crccheck/django-object-actions/commit/1595348d00235752857fef55f9fbbc8b854659d9))

- **ci**: Update [tool.semantic_release] names
  ([#160](https://github.com/crccheck/django-object-actions/pull/160),
  [`70d2c81`](https://github.com/crccheck/django-object-actions/commit/70d2c8110e3c087366a67c4499fa0895035fbdfd))

I missed some updated config changes -
  https://python-semantic-release.readthedocs.io/en/latest/migrating_from_v7.html#version-toml -
  https://python-semantic-release.readthedocs.io/en/latest/configuration.html#config-version-variables

### Chores

- Fix formatting in example app ([#155](https://github.com/crccheck/django-object-actions/pull/155),
  [`9bd288f`](https://github.com/crccheck/django-object-actions/commit/9bd288ffc6768bcf39ec27abde024b7be0ee90c9))

Ran black on to comply with format from 23.x version

- **ci**: Add Django 4.2 to the build matrix
  ([#154](https://github.com/crccheck/django-object-actions/pull/154),
  [`e73b4d0`](https://github.com/crccheck/django-object-actions/commit/e73b4d0d8921d566a880612f1622df87c99d062b))

- **ci**: Remove deprecated set-output syntax
  ([#146](https://github.com/crccheck/django-object-actions/pull/146),
  [`3e42b3b`](https://github.com/crccheck/django-object-actions/commit/3e42b3be4fdced017f23234b5da2c17373fbc50b))

fixes deprecation warnings in CI: > The `set-output` command is deprecated and will be disabled
  soon. Please upgrade to using Environment Files. For more information see:
  https://github.blog/changelog/2022-10-11-github-actions-deprecating-save-state-and-set-output-commands/

- **ci**: Upgrade python-semantic-release
  ([#145](https://github.com/crccheck/django-object-actions/pull/145),
  [`53417a0`](https://github.com/crccheck/django-object-actions/commit/53417a01bc78a9a7bb59f4599154d180914f064b))

Hopefully this fixes the broken GitHub Action too
  https://github.com/crccheck/django-object-actions/actions/runs/3464471740 `error: No module named
  'packaging'`

https://github.com/python-semantic-release/python-semantic-release/issues/489

closes #144

- **deps**: Refresh dev dependencies
  ([#158](https://github.com/crccheck/django-object-actions/pull/158),
  [`7d439b6`](https://github.com/crccheck/django-object-actions/commit/7d439b6910c2c30cd692bdb8819fe714f1b584a7))

Also moves Coverage config to `pyproject.toml` to eliminate another top level project file

### Documentation

- Update README style ([#157](https://github.com/crccheck/django-object-actions/pull/157),
  [`f92464e`](https://github.com/crccheck/django-object-actions/commit/f92464e43e195dc3dede7f1102cf02e08c2845df))

To reduce future diffs from autoformat

### Features

- Test release for new python-semantic-release process
  ([#159](https://github.com/crccheck/django-object-actions/pull/159),
  [`6af5f36`](https://github.com/crccheck/django-object-actions/commit/6af5f367deb0f6787459058edbfdc92c1108be4e))

Just upgrading to stay current. Need to use "feat" to trigger a release.

Docs: - https://python-semantic-release.readthedocs.io/en/latest/migrating_from_v7.html -
  https://github.com/pypa/gh-action-pypi-publish#usage


## v4.1.0 (2022-11-14)

### Bug Fixes

- Fix link to ci.yml in README ([#139](https://github.com/crccheck/django-object-actions/pull/139),
  [`700dd9b`](https://github.com/crccheck/django-object-actions/commit/700dd9b848aea67c759dca61cd815a27b6b16fd1))

Fix README link to ci.yml

### Chores

- **ci**: Add Python 3.11 and Django 4.1 to CI
  ([#143](https://github.com/crccheck/django-object-actions/pull/143),
  [`10e4743`](https://github.com/crccheck/django-object-actions/commit/10e4743ad3df72a85f7f11844d22ddbe091398cf))

Just some housekeeping and local dev tweaks.

### Features

- Provide action decorator to pass label, description and atts to the admin method
  ([#141](https://github.com/crccheck/django-object-actions/pull/141),
  [`5638f99`](https://github.com/crccheck/django-object-actions/commit/5638f999d32ea7f6de60b895d23ce89624120769))

Add an `@action` decorator that behave's like Django's `admin.action` decorator[^1] to clean up
  customizing object actions.

[closes #115](https://github.com/crccheck/django-object-actions/issues/115)

Also relates to #107

[^1]:
  https://docs.djangoproject.com/en/stable/ref/contrib/admin/actions/#django.contrib.admin.action


## v4.0.0 (2022-03-12)

### Bug Fixes

- Cleanup Django compatibility shims for <2.0
  ([#126](https://github.com/crccheck/django-object-actions/pull/126),
  [`88cfb3b`](https://github.com/crccheck/django-object-actions/commit/88cfb3b2e06b17762639da7f48259eeae343942f))

### Chores

- **deps**: Refresh dev deps and refactor CI
  ([#132](https://github.com/crccheck/django-object-actions/pull/132),
  [`6283e62`](https://github.com/crccheck/django-object-actions/commit/6283e621eebe55e22c72323fc1509bf77d93932d))

This updates CI to use https://github.com/fabiocaccamo/create-matrix-action to simplify the config
  file. Poetry's lock file updated as I reinstalled on a new computer.

### Documentation

- Add Django@4.0 to CI ([#133](https://github.com/crccheck/django-object-actions/pull/133),
  [`20e2418`](https://github.com/crccheck/django-object-actions/commit/20e2418e6ada4651b3e6d51b5d10c545d8a6c863))

* upgrade some more deps

* add django 4.0 to ci

* cleanup ci for Black

* fix poetry's python version conflicts with CI version

### Features

- Drop Python 3.6 support ([#135](https://github.com/crccheck/django-object-actions/pull/135),
  [`8deebed`](https://github.com/crccheck/django-object-actions/commit/8deebedda55d0e5d466969c7f27a9c60e680e5e8))

BREAKING CHANGE: Python 3.6 is past end-of-life and is no longer supported. Keeping it in
  `pyproject.toml` was causing pains trying to install packages. Let's drop it while we're dropping
  support for other old stuff.

### Breaking Changes

- Python 3.6 is past end-of-life and is no longer supported. Keeping it in `pyproject.toml` was
  causing pains trying to install packages. Let's drop it while we're dropping support for other old
  stuff.


## v3.1.0 (2021-12-18)

### Bug Fixes

- Fix typo in version_variable ([#130](https://github.com/crccheck/django-object-actions/pull/130),
  [`040a802`](https://github.com/crccheck/django-object-actions/commit/040a8029c298d8bb17ffab0b75b9b9ecc3d70de2))

Fix "error: [Errno 2] No such file or directory: 'django-object-actions/init.py'" error when
  creating a release

### Chores

- **ci**: Run some tests using Poetry build instead of source
  ([#129](https://github.com/crccheck/django-object-actions/pull/129),
  [`c24c299`](https://github.com/crccheck/django-object-actions/commit/c24c299470d055bd1e0cb9256d65b6b0a56ce7f3))

To verify that it's getting packaged correctly. In particular, I need to make sure the `.html` files
  are in the package.

### Features

- Add Python 3.9 & 3.10 support
  ([`28f0ef7`](https://github.com/crccheck/django-object-actions/commit/28f0ef7dd62eedbdac9d34ad115245ef8d935c4d))

* ci: add Python 3.9-310 to the build

* fix: support Python 3.9-3.10 in trove classifiers

- **ci**: Add manual semantic-release
  ([#128](https://github.com/crccheck/django-object-actions/pull/128),
  [`f43fd11`](https://github.com/crccheck/django-object-actions/commit/f43fd1199a72be013766d437fe54d875e2fdd53f))

I'll switch it to be automated on push to `master` at some point.

### Refactoring

- Switch to Poetry for env+dep management
  ([#127](https://github.com/crccheck/django-object-actions/pull/127),
  [`f16cb00`](https://github.com/crccheck/django-object-actions/commit/f16cb0089d172cfa9a84c49121fc434d84e21abe))

I've been using Poetry because it takes the hassle out of virtualenv management and has sane
  defaults that just work for building artifacts and uploading to PyPI.

Because I had to redo how tests were run, I went ahead and removed the Tox testing requirement too
  and so I had to redo the Github Actions for testing too.

One thing I didn't anticipate is that Github Actions caching doesn't work for Poetry, only with
  `requirements.txt` and Pipenv
  https://github.blog/changelog/2021-11-23-github-actions-setup-python-now-supports-dependency-caching/

## Verifying the change I compared `python setup.py build` vs `poetry build` and the only difference
  was some top level meta differences and Poetry added the `tests` directory which is fine. Both
  have the `.html` templates which is the important thing.


## v3.0.2 (2021-04-09)

### Chores

- Add Django 3.2 to test grid ([#117](https://github.com/crccheck/django-object-actions/pull/117),
  [`e473bc3`](https://github.com/crccheck/django-object-actions/commit/e473bc32777496d6e98e045b51f9d901384f4193))

https://docs.djangoproject.com/en/3.2/releases/3.2/

I really need to drop support for old versions now. Lots of deps are starting to step on each other
  and drop things. Django itself doesn't support Django 3.0 anymore with the release of Django 3.2

- **release**: 3.0.2
  ([`dbcecbf`](https://github.com/crccheck/django-object-actions/commit/dbcecbfe67254f6fff64e670c443a6c1d662a9ff))

### Refactoring

- Use django.urls.re_path instead of deprecated django.conf.urls.url
  ([#112](https://github.com/crccheck/django-object-actions/pull/112),
  [`9bb736a`](https://github.com/crccheck/django-object-actions/commit/9bb736a6ffb1e35ac3f441ff0d572ba6e13b447c))

Use `django.urls.re_path()` when available, instead of the deprecated `django.conf.urls.url()`.

* `re_path()` is available since Django 2.0. * `url()` will be removed in Django 4.0.


## v3.0.1 (2020-08-08)

### Bug Fixes

- Objects with special symbols in primary key 404-ed
  ([#110](https://github.com/crccheck/django-object-actions/pull/110),
  [`0c90ce1`](https://github.com/crccheck/django-object-actions/commit/0c90ce12a066baf873037eed415052074430d9d2))

for case if object in database has any of special symbols
  https://github.com/django/django/blob/master/django/contrib/admin/utils.py#L17 clicking on action
  button causes 404 error, as in SingleObjectMixin there are already parsed kwargs from url, and
  they are unquoted

made unquoting kwargs

### Chores

- **release**: 3.0.1
  ([`fa48985`](https://github.com/crccheck/django-object-actions/commit/fa48985e5da6acdc327eae72b97edcd387d8afba))


## v3.0.0 (2020-08-08)

### Chores

- **release**: 3.0.0
  ([`6b61513`](https://github.com/crccheck/django-object-actions/commit/6b615133608caab492fe13ec3403dab281520186))

### Features

- Add Django 3 test support ([#106](https://github.com/crccheck/django-object-actions/pull/106),
  [`4eaf14c`](https://github.com/crccheck/django-object-actions/commit/4eaf14c3caff36d5ab274835d38baef7e66213dc))

Django 3.0 is out: https://docs.djangoproject.com/en/3.0/releases/3.0/ Let's see if we're
  compatible. It turns out no code changes are needed huzzah!

- **deps**: Add Django 3.1 support
  ([#109](https://github.com/crccheck/django-object-actions/pull/109),
  [`2c7170e`](https://github.com/crccheck/django-object-actions/commit/2c7170e3a73317a9417733a7ddfe0fabab84fe85))

Pretty basic, looks like no code changes needed.

https://docs.djangoproject.com/en/3.1/releases/3.1/

- **deps**: Drop Python 3.4 support
  ([#108](https://github.com/crccheck/django-object-actions/pull/108),
  [`68519d4`](https://github.com/crccheck/django-object-actions/commit/68519d48fa8dd4d3b203981a52157841e5152774))

BREAKING CHANGE: drop Python 3.4 support in preparation for adding type hints and Django 3.1 support

Prereq for #107


## v2.0.0 (2019-11-29)

### Chores

- **release**: 2.0.0
  ([`9169f0d`](https://github.com/crccheck/django-object-actions/commit/9169f0df7298169179407859368f50453ec064f0))

### Features

- Drop Python 2 support ([#105](https://github.com/crccheck/django-object-actions/pull/105),
  [`551d2bb`](https://github.com/crccheck/django-object-actions/commit/551d2bb2a66c5fd1c157b05c288032124affba41))

BREAKING CHANGE: This release drops Python 2 support

Django has [dropped Python 2
  support](https://docs.djangoproject.com/en/2.2/releases/2.0/#python-compatibility) ever since
  Django 2.0 (December 2, 2017). With Django 3.0 coming very soon and Python 2 reaching end of life,
  it doesn't make sense to continue supporting Python 2.

### Breaking Changes

- This release drops Python 2 support


## v1.1.2 (2019-11-14)

### Chores

- Use Black to format code ([#100](https://github.com/crccheck/django-object-actions/pull/100),
  [`42055a3`](https://github.com/crccheck/django-object-actions/commit/42055a391044a3d828531cb0ab7ff6abe4f5a659))

There's a lot of momentum to using [Black](https://github.com/psf/black). For example, [Django will
  use it](https://github.com/django/deps/blob/master/accepted/0008-black.rst)

This pulls the bandaid off to avoid mixing lint changes w/ code changes in the future. I opted to
  not dictate how Black is run because I'm not 100% sure how that should happen. To make sure PRs
  contributors are following this, I added a lint check in CI.

- **release**: 1.1.2
  ([`0cd8a24`](https://github.com/crccheck/django-object-actions/commit/0cd8a24ac7ae90a169735e4035ce89701f7cff20))

### Documentation

- Add syntax highlighting ([#102](https://github.com/crccheck/django-object-actions/pull/102),
  [`399affa`](https://github.com/crccheck/django-object-actions/commit/399affa66664a65216c51346e96972eb5ae22499))


## v1.1.1 (2019-10-06)

### Bug Fixes

- Changelist action links had no 'href'
  ([#98](https://github.com/crccheck/django-object-actions/pull/98),
  [`8b8aed3`](https://github.com/crccheck/django-object-actions/commit/8b8aed3b131cf60bc8823c703299f50cf84d9dcc))

I probably copy pasted something wrong and brought an extra arg into the `reverse`, so `reverse`
  never found anything and the actions in the changelist never rendered with a `href`. This makes
  the args match the url definition so these buttons work again.

Thanks to @mvbrn for the original fix.

closes #96

### Chores

- Bump dev dependencies ([#95](https://github.com/crccheck/django-object-actions/pull/95),
  [`fceff29`](https://github.com/crccheck/django-object-actions/commit/fceff29fffb1fc962e19a3175cace3e9434cbd74))

* greenkeeper

* django-extensions is safe to upgrade now

* use consistent DJANGO<v> comment to indicate backwards compatibility

* exclude sqlite from docker too

* TODO

* don't email failures

- Modernize some syntax, add Django 2.2 and Py37
  ([#91](https://github.com/crccheck/django-object-actions/pull/91),
  [`ba9eb1b`](https://github.com/crccheck/django-object-actions/commit/ba9eb1b9fba5f6eebfbb605e9002c43bb0b6bfc8))

* greenkeeper

* add py37 and django2.1 to testing matrix

* update coveralls to use latest versions

* make sure to use factoryboy's version of Faker

* add versions to travisci

* use Factoryboy's fakersyntax

* ugh

* selective coveralls

* add Django 2.2

* disable coveralls in CI for nw

* only build on PRs and master

* don't commit .sqlite

* add missing setting

* fix broken test

* haha need a script to run tests


## v1.1.0 (2019-05-04)

### Features

- Make default labels prettier ([#93](https://github.com/crccheck/django-object-actions/pull/93),
  [`4191afd`](https://github.com/crccheck/django-object-actions/commit/4191afd691d9a70fd6b0de095477067cf3c35691))

With this change the default label changes from `some_action` to `Some action`


## v1.0.0 (2018-03-09)


## v0.10.0 (2017-05-10)


## v0.9.0 (2016-12-04)


## v0.8.2 (2016-04-23)


## v0.8.1 (2016-04-23)


## v0.8.0 (2016-02-25)


## v0.7.0 (2016-01-13)

### Documentation

- More tweaks as I read code
  ([`936fe08`](https://github.com/crccheck/django-object-actions/commit/936fe084054daf90ab2011c337aac02d2701b5a5))


## v0.6.0 (2015-12-06)


## v0.5.1 (2014-11-27)


## v0.5.0 (2014-07-01)


## v0.4.0 (2014-02-12)


## v0.3.0 (2014-01-09)


## v0.2.0 (2013-11-09)


## v0.1.1 (2013-02-26)


## v0.1.0 (2013-02-24)

### Bug Fixes

- Actions showed up in /add/, they shouldn't
  ([`bd23a60`](https://github.com/crccheck/django-object-actions/commit/bd23a6023b3358d6ec0a59b50774d1f5d5d422ed))

- Make sure not to include pyc files
  ([`d52f802`](https://github.com/crccheck/django-object-actions/commit/d52f8020024499df7e0bec6f7606707e9045b90b))
