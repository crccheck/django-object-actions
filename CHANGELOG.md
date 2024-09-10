# CHANGELOG

## v4.3.0 (2024-09-10)

### Chore

* chore(ci): upgrade python-semantic-release to v9.8.8 (#176)

There have been a lot of releases since v8.0.8
https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md#v808-2023-08-26

The breaking change was dropping Python 3.7. While this project supports
3.7... that will change the next opportunity ([`50a03af`](https://github.com/crccheck/django-object-actions/commit/50a03afdf1571a5cb17db282df089f81a3c20ad2))

* chore: update Django/Python test matrix and add classifier for py3.12 (#171) ([`ad3b898`](https://github.com/crccheck/django-object-actions/commit/ad3b8987c5b20391c3e5b56147c799e9aa4804bd))

* chore: add Django v5 to CI matrix (#166)

https://docs.djangoproject.com/en/5.0/releases/5.0/ ([`b63aac1`](https://github.com/crccheck/django-object-actions/commit/b63aac1e919c986df9687699c6494dab3093b295))

### Documentation

* docs: add Django Modal Actions as a similar package (#173)

Adding new Django Modal Actions package
Deleting Django Object Actions which hasn&#39;t had a commit in 3 years ([`813687e`](https://github.com/crccheck/django-object-actions/commit/813687e76241f8a6786fa20ea707ae470f1463ab))

### Feature

* feat: add a way to make a POST only action (#174)

Followup to #168 to get CI to pass again, documents how to make a POST
only action, and adds some test coverage.

There are still a few cleanup issues but this should get things moving
on POST only actions again. ([`494d581`](https://github.com/crccheck/django-object-actions/commit/494d5817307343018ccc8398d64f95228e57f51b))

### Style

* style: apply Black formatting (#170) ([`fb3ce5b`](https://github.com/crccheck/django-object-actions/commit/fb3ce5b75bda44dfd3185c25e9cf7e943ca6fb61))

### Unknown

* wip to select GET or POST for actions (#168)

Another try at enforcing POST actions. This change is more gradual than
#149 - when library user doesn&#39;t change default options the behavior is
exactly the same as before the change, that is:

1. Action buttons send GET requests
2. Action handlers accept GET and POST requests

However, user can change this behavior using `methods` and `button_type`
kwargs. For example `@action(methods=[&#39;POST&#39;], button_type=&#39;form&#39;)`
results in

1. Action button sends POST requests
2. Action handler accepts only POST request

Unfortunately I have this tested only within my project. Also the docs
are missing.

And one more thing - I think it is better to use `&lt;input type=&#34;submit&#34;&gt;`
instead of js to submit the form. This js is need to make the buttons
look the same in both versions. With proper CSS (that is beyond my
ability to write ;) ) js is avoidable and we could be using pretty
semantic html submit button. I took the form button template from #149. ([`1274ae7`](https://github.com/crccheck/django-object-actions/commit/1274ae7f9743564cd0f36a34265c9c2f8e98fce3))

## v4.2.0 (2023-09-08)

### Chore

* chore(deps): refresh dev dependencies (#158)

Also moves Coverage config to `pyproject.toml` to eliminate another top
level project file ([`7d439b6`](https://github.com/crccheck/django-object-actions/commit/7d439b6910c2c30cd692bdb8819fe714f1b584a7))

* chore(ci): add Django 4.2 to the build matrix (#154) ([`e73b4d0`](https://github.com/crccheck/django-object-actions/commit/e73b4d0d8921d566a880612f1622df87c99d062b))

* chore: fix formatting in example app (#155)

Ran black on to comply with format from 23.x version ([`9bd288f`](https://github.com/crccheck/django-object-actions/commit/9bd288ffc6768bcf39ec27abde024b7be0ee90c9))

* chore(ci): remove deprecated set-output syntax (#146)

fixes deprecation warnings in CI:
&gt; The `set-output` command is deprecated and will be disabled soon.
Please upgrade to using Environment Files. For more information see:
https://github.blog/changelog/2022-10-11-github-actions-deprecating-save-state-and-set-output-commands/ ([`3e42b3b`](https://github.com/crccheck/django-object-actions/commit/3e42b3be4fdced017f23234b5da2c17373fbc50b))

* chore(ci): upgrade python-semantic-release (#145)

Hopefully this fixes the broken GitHub Action too
https://github.com/crccheck/django-object-actions/actions/runs/3464471740
`error: No module named &#39;packaging&#39;`


https://github.com/python-semantic-release/python-semantic-release/issues/489

closes #144 ([`53417a0`](https://github.com/crccheck/django-object-actions/commit/53417a01bc78a9a7bb59f4599154d180914f064b))

### Documentation

* docs: update README style (#157)

To reduce future diffs from autoformat ([`f92464e`](https://github.com/crccheck/django-object-actions/commit/f92464e43e195dc3dede7f1102cf02e08c2845df))

### Feature

* feat: test release for new python-semantic-release process (#159)

Just upgrading to stay current. Need to use &#34;feat&#34; to trigger a release.

Docs:
-
https://python-semantic-release.readthedocs.io/en/latest/migrating_from_v7.html
- https://github.com/pypa/gh-action-pypi-publish#usage ([`6af5f36`](https://github.com/crccheck/django-object-actions/commit/6af5f367deb0f6787459058edbfdc92c1108be4e))

### Fix

* fix(ci): maybe this will fix Semantic Release (#161) ([`1595348`](https://github.com/crccheck/django-object-actions/commit/1595348d00235752857fef55f9fbbc8b854659d9))

* fix(ci): update [tool.semantic_release] names (#160)

I missed some updated config changes
-
https://python-semantic-release.readthedocs.io/en/latest/migrating_from_v7.html#version-toml
-
https://python-semantic-release.readthedocs.io/en/latest/configuration.html#config-version-variables ([`70d2c81`](https://github.com/crccheck/django-object-actions/commit/70d2c8110e3c087366a67c4499fa0895035fbdfd))

## v4.1.0 (2022-11-14)

### Chore

* chore(ci): add Python 3.11 and Django 4.1 to CI (#143)

Just some housekeeping and local dev tweaks. ([`10e4743`](https://github.com/crccheck/django-object-actions/commit/10e4743ad3df72a85f7f11844d22ddbe091398cf))

### Feature

* feat: provide action decorator to pass label, description and atts to the admin method  (#141)

Add an `@action` decorator that behave&#39;s like Django&#39;s `admin.action` decorator[^1] to clean up customizing object actions.

[closes #115](https://github.com/crccheck/django-object-actions/issues/115)

Also relates to #107

[^1]: https://docs.djangoproject.com/en/stable/ref/contrib/admin/actions/#django.contrib.admin.action ([`5638f99`](https://github.com/crccheck/django-object-actions/commit/5638f999d32ea7f6de60b895d23ce89624120769))

### Fix

* fix: fix link to ci.yml in README (#139)

Fix README link to ci.yml ([`700dd9b`](https://github.com/crccheck/django-object-actions/commit/700dd9b848aea67c759dca61cd815a27b6b16fd1))

## v4.0.0 (2022-03-12)

### Breaking

* feat!: drop Python 3.6 support (#135)

BREAKING CHANGE: Python 3.6 is past end-of-life and is no longer supported. Keeping it in `pyproject.toml` was causing pains trying to install packages. Let&#39;s drop it while we&#39;re dropping support for other old stuff. ([`8deebed`](https://github.com/crccheck/django-object-actions/commit/8deebedda55d0e5d466969c7f27a9c60e680e5e8))

### Chore

* chore(deps): refresh dev deps and refactor CI (#132)

This updates CI to use https://github.com/fabiocaccamo/create-matrix-action to simplify the config file. Poetry&#39;s lock file updated as I reinstalled on a new computer. ([`6283e62`](https://github.com/crccheck/django-object-actions/commit/6283e621eebe55e22c72323fc1509bf77d93932d))

### Documentation

* docs: add Django@4.0 to CI  (#133)

* upgrade some more deps

* add django 4.0 to ci

* cleanup ci for Black

* fix poetry&#39;s python version conflicts with CI version ([`20e2418`](https://github.com/crccheck/django-object-actions/commit/20e2418e6ada4651b3e6d51b5d10c545d8a6c863))

### Fix

* fix: cleanup Django compatibility shims for &lt;2.0 (#126) ([`88cfb3b`](https://github.com/crccheck/django-object-actions/commit/88cfb3b2e06b17762639da7f48259eeae343942f))

## v3.1.0 (2021-12-18)

### Chore

* chore(ci): run some tests using Poetry build instead of source (#129)

To verify that it&#39;s getting packaged correctly. In particular, I need to make sure the `.html` files are in the package. ([`c24c299`](https://github.com/crccheck/django-object-actions/commit/c24c299470d055bd1e0cb9256d65b6b0a56ce7f3))

### Feature

* feat(ci): add manual semantic-release (#128)

I&#39;ll switch it to be automated on push to `master` at some point. ([`f43fd11`](https://github.com/crccheck/django-object-actions/commit/f43fd1199a72be013766d437fe54d875e2fdd53f))

* feat: Add Python 3.9 &amp; 3.10 support

* ci: add Python 3.9-310 to the build

* fix: support Python 3.9-3.10 in trove classifiers ([`28f0ef7`](https://github.com/crccheck/django-object-actions/commit/28f0ef7dd62eedbdac9d34ad115245ef8d935c4d))

### Fix

* fix: fix typo in version_variable (#130)

Fix &#34;error: [Errno 2] No such file or directory: &#39;django-object-actions/init.py&#39;&#34; error when creating a release ([`040a802`](https://github.com/crccheck/django-object-actions/commit/040a8029c298d8bb17ffab0b75b9b9ecc3d70de2))

### Refactor

* refactor: switch to Poetry for env+dep management (#127)

I&#39;ve been using Poetry because it takes the hassle out of virtualenv management and has sane defaults that just work for building artifacts and uploading to PyPI.

Because I had to redo how tests were run, I went ahead and removed the Tox testing requirement too and so I had to redo the Github Actions for testing too.

One thing I didn&#39;t anticipate is that Github Actions caching doesn&#39;t work for Poetry, only with `requirements.txt` and Pipenv https://github.blog/changelog/2021-11-23-github-actions-setup-python-now-supports-dependency-caching/

## Verifying the change
I compared `python setup.py build` vs `poetry build` and the only difference was some top level meta differences and Poetry added the `tests` directory which is fine. Both have the `.html` templates which is the important thing. ([`f16cb00`](https://github.com/crccheck/django-object-actions/commit/f16cb0089d172cfa9a84c49121fc434d84e21abe))

### Unknown

* Migrate CI to GitHub actions (#122)

TravisCI stopped building 7 months ago, migrate to GitHub actions which seems to be the default choice these days. Some comments about this change:

- I tried to keep the build matrix close to how it was but [the build failed](https://github.com/browniebroke/django-object-actions/actions/runs/1431603631) for Django&lt;2, so I&#39;ve dropped these versions. 
- Python 3.5 reached the end of its life on September 13th, 2020, so I&#39;ve dropped it as well.
- The build status isn&#39;t reported in this PR because it&#39;s a new workflow added from a fork, and GitHub doesn&#39;t run it for security reasons. You can see the [build results in my fork](https://github.com/browniebroke/django-object-actions/actions).
- I didn&#39;t bother trying to add new versions for now, can be done separately. ([`4340c89`](https://github.com/crccheck/django-object-actions/commit/4340c8958492dfd2e6113fcba6fdcdc90be02e8e))

## v3.0.2 (2021-04-09)

### Chore

* chore(release): 3.0.2 ([`dbcecbf`](https://github.com/crccheck/django-object-actions/commit/dbcecbfe67254f6fff64e670c443a6c1d662a9ff))

* chore: add Django 3.2 to test grid (#117)

https://docs.djangoproject.com/en/3.2/releases/3.2/

I really need to drop support for old versions now. Lots of deps are starting to step on each other and drop things. Django itself doesn&#39;t support Django 3.0 anymore with the release of Django 3.2 ([`e473bc3`](https://github.com/crccheck/django-object-actions/commit/e473bc32777496d6e98e045b51f9d901384f4193))

### Refactor

* refactor: Use django.urls.re_path instead of deprecated django.conf.urls.url (#112)

Use `django.urls.re_path()` when available, instead of the deprecated `django.conf.urls.url()`.

* `re_path()` is available since Django 2.0.
* `url()` will be removed in Django 4.0. ([`9bb736a`](https://github.com/crccheck/django-object-actions/commit/9bb736a6ffb1e35ac3f441ff0d572ba6e13b447c))

## v3.0.1 (2020-08-08)

### Chore

* chore(release): 3.0.1 ([`fa48985`](https://github.com/crccheck/django-object-actions/commit/fa48985e5da6acdc327eae72b97edcd387d8afba))

### Fix

* fix: Objects with special symbols in primary key 404-ed (#110)

for case if object in database has any of special symbols
https://github.com/django/django/blob/master/django/contrib/admin/utils.py#L17
clicking on action button causes 404 error, as in SingleObjectMixin there are already parsed kwargs from url, and they are unquoted

made unquoting kwargs ([`0c90ce1`](https://github.com/crccheck/django-object-actions/commit/0c90ce12a066baf873037eed415052074430d9d2))

## v3.0.0 (2020-08-08)

### Breaking

* feat(deps): Drop Python 3.4 support (#108)

BREAKING CHANGE: drop Python 3.4 support in preparation for adding type hints and Django 3.1 support

Prereq for #107 ([`68519d4`](https://github.com/crccheck/django-object-actions/commit/68519d48fa8dd4d3b203981a52157841e5152774))

### Chore

* chore(release): 3.0.0 ([`6b61513`](https://github.com/crccheck/django-object-actions/commit/6b615133608caab492fe13ec3403dab281520186))

### Feature

* feat(deps): Add Django 3.1 support (#109)

Pretty basic, looks like no code changes needed.

https://docs.djangoproject.com/en/3.1/releases/3.1/ ([`2c7170e`](https://github.com/crccheck/django-object-actions/commit/2c7170e3a73317a9417733a7ddfe0fabab84fe85))

* feat: add Django 3 test support (#106)

Django 3.0 is out: https://docs.djangoproject.com/en/3.0/releases/3.0/ Let&#39;s see if we&#39;re compatible. It turns out no code changes are needed huzzah! ([`4eaf14c`](https://github.com/crccheck/django-object-actions/commit/4eaf14c3caff36d5ab274835d38baef7e66213dc))

## v2.0.0 (2019-11-29)

### Breaking

* feat: Drop Python 2 support (#105)

BREAKING CHANGE: This release drops Python 2 support

Django has [dropped Python 2 support](https://docs.djangoproject.com/en/2.2/releases/2.0/#python-compatibility) ever since Django 2.0 (December 2, 2017). With Django 3.0 coming very soon and Python 2 reaching end of life, it doesn&#39;t make sense to continue supporting Python 2. ([`551d2bb`](https://github.com/crccheck/django-object-actions/commit/551d2bb2a66c5fd1c157b05c288032124affba41))

### Chore

* chore(release): 2.0.0 ([`9169f0d`](https://github.com/crccheck/django-object-actions/commit/9169f0df7298169179407859368f50453ec064f0))

## v1.1.2 (2019-11-14)

### Chore

* chore(release): 1.1.2 ([`0cd8a24`](https://github.com/crccheck/django-object-actions/commit/0cd8a24ac7ae90a169735e4035ce89701f7cff20))

* chore: Use Black to format code (#100)

There&#39;s a lot of momentum to using [Black](https://github.com/psf/black). For example, [Django will use it](https://github.com/django/deps/blob/master/accepted/0008-black.rst)

This pulls the bandaid off to avoid mixing lint changes w/ code changes in the future. I opted to not dictate how Black is run because I&#39;m not 100% sure how that should happen. To make sure PRs contributors are following this, I added a lint check in CI. ([`42055a3`](https://github.com/crccheck/django-object-actions/commit/42055a391044a3d828531cb0ab7ff6abe4f5a659))

### Documentation

* docs: add syntax highlighting  (#102) ([`399affa`](https://github.com/crccheck/django-object-actions/commit/399affa66664a65216c51346e96972eb5ae22499))

### Unknown

* change README to Markdown to simplify things (#104)

I&#39;m not planning on doing a Sphinx site, so let&#39;s use Markdown to make the documentation easier to maintain.

Part of #94 ([`2d2a689`](https://github.com/crccheck/django-object-actions/commit/2d2a689a0dd8d829ca84ffaee73b753473175935))

## v1.1.1 (2019-10-06)

### Chore

* chore: bump dev dependencies (#95)

* greenkeeper

* django-extensions is safe to upgrade now

* use consistent DJANGO&lt;v&gt; comment to indicate backwards compatibility

* exclude sqlite from docker too

* TODO

* greenkeeper

* don&#39;t email failures ([`fceff29`](https://github.com/crccheck/django-object-actions/commit/fceff29fffb1fc962e19a3175cace3e9434cbd74))

* chore: modernize some syntax, add Django 2.2 and Py37 (#91)

* greenkeeper

* add py37 and django2.1 to testing matrix

* update coveralls to use latest versions

* make sure to use factoryboy&#39;s version of Faker

* add versions to travisci

* use Factoryboy&#39;s fakersyntax

* ugh

* selective coveralls

* add Django 2.2

* disable coveralls in CI for nw

* only build on PRs and master

* don&#39;t commit .sqlite

* add missing setting

* fix broken test

* haha need a script to run tests ([`ba9eb1b`](https://github.com/crccheck/django-object-actions/commit/ba9eb1b9fba5f6eebfbb605e9002c43bb0b6bfc8))

### Fix

* fix: changelist action links had no &#39;href&#39; (#98)

I probably copy pasted something wrong and brought an extra arg into the `reverse`, so `reverse` never found anything and the actions in the changelist never rendered with a `href`. This makes the args match the url definition so these buttons work again.

Thanks to @mvbrn for the original fix.

closes #96 ([`8b8aed3`](https://github.com/crccheck/django-object-actions/commit/8b8aed3b131cf60bc8823c703299f50cf84d9dcc))

### Unknown

* v1.1.1 (#99) ([`1226ca1`](https://github.com/crccheck/django-object-actions/commit/1226ca105e9e13a43a6b8a1562af0993c49a7081))

## v1.1.0 (2019-05-04)

### Feature

* feat: Make default labels prettier (#93)

With this change the default label changes from `some_action` to `Some action` ([`4191afd`](https://github.com/crccheck/django-object-actions/commit/4191afd691d9a70fd6b0de095477067cf3c35691))

### Unknown

* bump version to v1.1.0 ([`78df3fc`](https://github.com/crccheck/django-object-actions/commit/78df3fc21358d54dbcc3bf690cc6638d6902be28))

* Return to preserved filters on change_list after object action (#88)

If you want to filter change_list by some conditions,
then open each object and run some object action there,
you will be returned to change_list with the same preserved filters.

Fix #83 

* Return to preserved filters on change_list after object action

* Changes after pull request: Load add_preserved_filters from admin_urls

* Changes after pull request: Indentation presumably reverted to original style ([`fb90869`](https://github.com/crccheck/django-object-actions/commit/fb908697a609f46889af15b543d444e5e19d6be2))

## v1.0.0 (2018-03-09)

### Unknown

* bump version to v1.0.0 ([`a390027`](https://github.com/crccheck/django-object-actions/commit/a3900271013abfab55a7082ff04586c9c3fee4d6))

* Cleanup random Django version support docs (#86)

No code changes, just:

* upgrade dev dependencies
* unify django version specific code comments to be `DJANGO&lt;version&gt;`
* update workflows to use more modern versions


#### Verifying change

* `make build`
* `make run`
* Browse to localhost:8000/admin/
* login with `admin`/`admin` ([`a7b183f`](https://github.com/crccheck/django-object-actions/commit/a7b183f3c1903cd11335d3fe166f90cc993da53b))

* Add support for Django 2.0 (#85)

Adding support for Django 2.0+, and removing support for Django versions up to 1.8, the oldest supported LTS release. This allows us to replace the now deprecated django-extensions UUIDField with the Django native version, and drop a couple of other hacks. Resolves #84 ([`430be02`](https://github.com/crccheck/django-object-actions/commit/430be02e59c8844f278f0749d840904137347eb3))

* Add a redirect example to the README (#82)

* use pip-tools to document requirements

* greenkeeper

* python 3.6 is a thing

* add a copy-paste ready example for HttpResponseRedirect action

* ugh, travisci

* try this shit out

* i guess it worked ([`81af3e7`](https://github.com/crccheck/django-object-actions/commit/81af3e7cd5b8f5c62a9a6d71ab2aaf657a6ac550))

## v0.10.0 (2017-05-10)

### Unknown

* bump version to v0.10.0 ([`8558f7b`](https://github.com/crccheck/django-object-actions/commit/8558f7bda66421c76ac2afe6b1d5e133b741944c))

* Release prep (#80)

* greenkeeper

* simplify tox deps

* add missing travisci coverage

* update docker demos

* standardize django version comments ([`242cf07`](https://github.com/crccheck/django-object-actions/commit/242cf071c1e4e6175bece2ed9619d9be2cd51d98))

* Get rid of Django 2.0 DeprecationWarning (#78)

* Get rid of Django 2.0 DeprecationWarning

Add 1.11 tox env

* add missing compatibility imports and reorder for readability ([`d3fb875`](https://github.com/crccheck/django-object-actions/commit/d3fb87558bf4309f5529dc7b3e85e0ccf1f5b1e4))

* Fix ``faker`` in requirements (#76)

Tests failed with
```
ImportError: The ``fake-factory`` package is now called ``Faker``.

Please update your requirements.
```
The `fake-factory` package was deprecated on December 15th, 2016.
Use the `Faker` package instead. ([`011ed07`](https://github.com/crccheck/django-object-actions/commit/011ed0758d17a31ca25b0f05dc4480ad5398251c))

## v0.9.0 (2016-12-04)

### Unknown

* bump version to v0.9.0 ([`8780870`](https://github.com/crccheck/django-object-actions/commit/878087064603e0df8305d3bb9d7696b6334fb530))

* Add support for all primary key formats (#75)

* support pks that are strings

* change pattern to be the same as what the Django admin uses ([`61fb1e5`](https://github.com/crccheck/django-object-actions/commit/61fb1e572d5b0a5a895603b6ebb2731f4e9c586e))

* Add Django 1.10 to &#39;tox&#39; support (#74)

* add django 1.10 to tox coverage

* Update &#39;make clean&#39; to clean python 3 files

* update test project for Django 1.10

* greenkeeper ([`38905d0`](https://github.com/crccheck/django-object-actions/commit/38905d0a0e596510e700e93333a9886a2ffb1389))

* Remove old things that were breaking the test suite (#73)

* drop testing for django 1.5

* delete django 1.5 hacks

* remove python 2.6 test coverage since it was broken ([`f9ed6ec`](https://github.com/crccheck/django-object-actions/commit/f9ed6ecf5ee8f5453a55f1c799c0ff334f395f6a))

* Fixed method name in changelog: get_objectactions -&gt; get_object_actions. (#71)

typo fix ([`ebe9442`](https://github.com/crccheck/django-object-actions/commit/ebe944244be30c0b3530031872061e9d43a1a331))

* Doc: clarify what row-actions package does (#70) ([`8969e2f`](https://github.com/crccheck/django-object-actions/commit/8969e2fb048877665c9f0640f24e7033dd17f750))

## v0.8.2 (2016-04-23)

### Unknown

* bump version to v0.8.2 ([`9537c41`](https://github.com/crccheck/django-object-actions/commit/9537c4154a05884076e10d642c86ceff7cea6b0a))

* fix django template settings be just using defaults (#65)

seriously, stop complaining about things I don&#39;t care about ([`73f1f44`](https://github.com/crccheck/django-object-actions/commit/73f1f44534569a877849da411e64ed5e64482aab))

## v0.8.1 (2016-04-23)

### Unknown

* bump version to v0.8.1 ([`809c7b0`](https://github.com/crccheck/django-object-actions/commit/809c7b0447a4fc6f475a2622abcf6c8c6b14314d))

* Fix how extra context set by admins was not passed (#64)

* refactor admin to organize things better

* add failing test case for extra context

s

* fixing context data ([`fe8ce91`](https://github.com/crccheck/django-object-actions/commit/fe8ce917412a095e4009faac4ada68e0ee8ee885))

* add ability redirect back active admin (#62)

* add ability redirect back active admin

when used several admins, you always redirect to default `admin`, should redirect back to active admin

* add tests for redirect back on multiple admin ([`bc4b38b`](https://github.com/crccheck/django-object-actions/commit/bc4b38ba30fe75e2482f8ebf19379de8ae4f1402))

* delete django 1.4 compatibility code (#63) ([`855c15f`](https://github.com/crccheck/django-object-actions/commit/855c15f5b9521a4e8eb3a1df5e07a1a2798665dc))

## v0.8.0 (2016-02-25)

### Unknown

* bump version to v0.8.0 ([`6612a24`](https://github.com/crccheck/django-object-actions/commit/6612a24d02b8d64c647eb71339a7cc3bf42109af))

* Fix the docker images so they start ready to go. Closes #58

Squashed commit of the following:

commit a9a6e11561b848112ff24252be5874e61942fbd2
Author: crccheck &lt;c@crccheck.com&gt;
Date:   Thu Feb 25 18:06:45 2016 -0600

    doc the Dock

commit acaae613237b0e4d9db016c49a32aa56865d4600
Author: crccheck &lt;c@crccheck.com&gt;
Date:   Thu Feb 25 17:53:04 2016 -0600

    switch to smaller base image and cacheable layers

commit 0fc71148d1c1289b0d4d7572499cfe686297799a
Author: crccheck &lt;c@crccheck.com&gt;
Date:   Thu Feb 25 17:46:37 2016 -0600

    doc how to upload images

commit 01fa29545c0fde269e82e212c8a821f017e39faf
Author: crccheck &lt;c@crccheck.com&gt;
Date:   Thu Feb 25 17:27:36 2016 -0600

    ugh

commit dc354981741c0e9e932fe46bdcf9bd68d8ca11db
Author: crccheck &lt;c@crccheck.com&gt;
Date:   Thu Feb 25 17:24:27 2016 -0600

    create a default admin/admin user

commit 8a492504182d820601afbbce3034d533cbb6bd41
Author: crccheck &lt;c@crccheck.com&gt;
Date:   Thu Feb 25 17:10:12 2016 -0600

    fix how the docker images didn&#39;t have a database ([`de1b76b`](https://github.com/crccheck/django-object-actions/commit/de1b76b3e32e1a11de11341d929dcc650c76b8fd))

* Add actions to the changelist admin page Closes #55

Squashed commit of the following:

commit c253a79cbf696b30e80f8fe454fea2e63031d2be
Author: crccheck &lt;c@crccheck.com&gt;
Date:   Sun Feb 21 09:52:53 2016 -0600

    update changelog

commit 433d0a29ca96ed4de565db0d36521acd7c5095c1
Author: crccheck &lt;c@crccheck.com&gt;
Date:   Sat Feb 20 23:37:09 2016 -0600

    rename more tools things to actions

commit 47e0eaac8e6e7f4d9aa39950fc3069149bfa03be
Author: crccheck &lt;c@crccheck.com&gt;
Date:   Sat Feb 20 21:56:49 2016 -0600

    readme update pass

commit 94ce625d4fb3e9fc6cfb0b6b8e0db924d64c0ee4
Author: crccheck &lt;c@crccheck.com&gt;
Date:   Sat Feb 20 21:26:33 2016 -0600

    refactor: re-arrangement

commit 324255a53e8a9289122298a361c65e1aa61307fc
Author: crccheck &lt;c@crccheck.com&gt;
Date:   Sat Feb 20 21:15:28 2016 -0600

    note about security

commit 67796ff2024ad6519566e5650c60fd9905acfcc8
Author: crccheck &lt;c@crccheck.com&gt;
Date:   Sat Feb 20 19:14:56 2016 -0600

    revamp get_change_action example to use real code

commit e300918c65691ae9e251f8655dc1692882142e8d
Author: crccheck &lt;c@crccheck.com&gt;
Date:   Sat Feb 20 10:44:02 2016 -0600

    rename get_object_actions since it broke anyways

commit c0a63b8e58aa46a9341373e9cb32990cafcc71c4
Author: crccheck &lt;c@crccheck.com&gt;
Date:   Sat Feb 20 09:29:49 2016 -0600

    documentation pass

commit 3a519b28a2e5e02fd224f247603e74dd36a4344d
Author: crccheck &lt;c@crccheck.com&gt;
Date:   Sat Feb 20 09:09:42 2016 -0600

    stub changelog

commit 823a5e29cf6a4fae1f11552424509a8a0c765a34
Author: crccheck &lt;c@crccheck.com&gt;
Date:   Fri Feb 19 23:51:03 2016 -0600

    refactor: dry

commit 594b8718010513da5b4b7945ddf44bb55c9e305b
Author: crccheck &lt;c@crccheck.com&gt;
Date:   Fri Feb 19 23:01:47 2016 -0600

    wire button to a new view

commit ff89b413bb0ce85b739f885fc3279cab46849a9b
Author: crccheck &lt;c@crccheck.com&gt;
Date:   Fri Feb 19 22:50:29 2016 -0600

    add changelist button

commit 22d6a8d02037bac489ee6dedb541581f815181b8
Author: crccheck &lt;c@crccheck.com&gt;
Date:   Fri Feb 19 22:26:13 2016 -0600

    flesh out the changelist actions

commit 7976c96f4dc1035cd2066d39c58a6597092f52db
Author: crccheck &lt;c@crccheck.com&gt;
Date:   Fri Feb 19 21:39:38 2016 -0600

    use a better place to get into the template context

    render_change_form works, but change_view is documented

commit 888725e8b35c8484244fec84c1ca83e292e8ad30
Author: crccheck &lt;c@crccheck.com&gt;
Date:   Wed Jan 13 23:08:54 2016 -0600

    use a more standard hook for extra context

commit b47e956a2f4de243e19ae46ef726239284c6bbfe
Author: crccheck &lt;c@crccheck.com&gt;
Date:   Wed Jan 13 22:45:47 2016 -0600

    pep8 ([`98aad50`](https://github.com/crccheck/django-object-actions/commit/98aad50f07f167de41ec0fa4fc348de3132840c5))

* Merge pull request #52 from ixc/master

Fixed example in documentation that doesn&#39;t work as advertised. ([`648c388`](https://github.com/crccheck/django-object-actions/commit/648c3885c5b50b0cd238aea77dff6559b1630aef))

* A slightly better way to express the logic in the example. ([`f6ff8f7`](https://github.com/crccheck/django-object-actions/commit/f6ff8f78c135cf108473ca36e14de46f1fdfd42c))

* Fixed example in documentation that doesn&#39;t work as advertised.

The context will _always_ have an &#39;original&#39; key if coming from Django&#39;s .changeform_view(), but it will be None if a new object is being added. ([`b49d08d`](https://github.com/crccheck/django-object-actions/commit/b49d08d34a6b59db60bade8221e4b9302e8cab20))

## v0.7.0 (2016-01-13)

### Documentation

* docs: more tweaks as I read code ([`936fe08`](https://github.com/crccheck/django-object-actions/commit/936fe084054daf90ab2011c337aac02d2701b5a5))

### Unknown

* bump version to v0.7.0 ([`a923cf2`](https://github.com/crccheck/django-object-actions/commit/a923cf25b37e268ddbeb5d4bb05ffb8c35cac182))

* Merge pull request #50 from crccheck/all-http-responses

All the http responses ([`a07159e`](https://github.com/crccheck/django-object-actions/commit/a07159e0c0dfbc9bc84c5644bc549e1b4a44f697))

* update travis with new tox env list ([`3785cf9`](https://github.com/crccheck/django-object-actions/commit/3785cf9dfb99394f06cf4100f1fbe2dd3d89ab6e))

* consistent quotes in setup.py ([`4279852`](https://github.com/crccheck/django-object-actions/commit/4279852d8cb236c3fd269e614463f1cedada8e98))

* allow streaming http response too

closes #38 ([`4b993f2`](https://github.com/crccheck/django-object-actions/commit/4b993f21362d389fc4accbbf6cffca6b0a6461c0))

* Merge pull request #49 from crccheck/fix-unnamed-admin-urls

Fix unnamed admin urls ([`310d086`](https://github.com/crccheck/django-object-actions/commit/310d08657b24e15ae61ce16bc21dcacba464adaf))

* delete unnecessary variable ([`0efc304`](https://github.com/crccheck/django-object-actions/commit/0efc304870a92cec7b89b62576074954f67873a9))

* fix bug with nameless admin urls ([`26f9362`](https://github.com/crccheck/django-object-actions/commit/26f936282f46c7e814eb7a2c5775227293ff1cea))

* add trivial test case for get_tool_urls ([`0022992`](https://github.com/crccheck/django-object-actions/commit/0022992ca3229c736951a90e99efc6b9098ed75e))

* update docs as I re-learn what&#39;s going on ([`e7903ae`](https://github.com/crccheck/django-object-actions/commit/e7903ae882d90a5568ce37d6dc05b2041a580557))

* Merge pull request #46 from Cuuuurzel/patch-1

Fixed urls patterns usage warning in Django 1.9 ([`22681a8`](https://github.com/crccheck/django-object-actions/commit/22681a8581993d0606bbc9e06f5d1d7e1cef1116))

* Fixed urls patterns usage warning in Django 1.0

Removed usage of django.conf.urls.patterns, in order to avoid warning :
&#34;&#34;&#34;
RemovedInDjango110Warning: django.conf.urls.patterns() is deprecated and will be removed in Django 1.10. Update your urlpatterns to be a list of django.conf.urls.url() instances instead.
&#34;&#34;&#34; ([`38a6e2b`](https://github.com/crccheck/django-object-actions/commit/38a6e2bfe4b0ed4651f6b53721d97b9af466771c))

* Merge pull request #48 from crccheck/maintenance

Requirements tweaks and Dockerfile ([`4c3915d`](https://github.com/crccheck/django-object-actions/commit/4c3915db5ea77332c5e1f10b94087583746c25fa))

* cleanup ([`0cdd715`](https://github.com/crccheck/django-object-actions/commit/0cdd7153648c8bf39437fafa515c1f61c258d733))

* transition away from having a hard Django dev dependency ([`074fb77`](https://github.com/crccheck/django-object-actions/commit/074fb7746e7b1d36f339c19e94fb7d356de527a5))

* add some Docker images to make it easier to try against multiple versions of Django ([`b34a944`](https://github.com/crccheck/django-object-actions/commit/b34a94474f1dfb319234ceeb8dfc51359a48350e))

* update copyright ([`28dacab`](https://github.com/crccheck/django-object-actions/commit/28dacabf6f7ab99ab2361e7dccbb80ac3e9353a3))

* remove Heroku quickstart since the free tier is dead ([`675e477`](https://github.com/crccheck/django-object-actions/commit/675e4775da906fff9a1289eee44802146ada4615))

* bump requirements to stay current ([`7c3dded`](https://github.com/crccheck/django-object-actions/commit/7c3ddeda01fe8d2198ebb4f745025d1dfe748c86))

* refactor Makefile help to be more compact ([`0feaaec`](https://github.com/crccheck/django-object-actions/commit/0feaaecf157c1f940548f04644add10c42d706cf))

* convert to using a VERSION file instead of a make variable ([`8fbd035`](https://github.com/crccheck/django-object-actions/commit/8fbd035c8b69881a5de6fc6cbd7ab52eac80cf02))

## v0.6.0 (2015-12-06)

### Unknown

* bump version to v0.6.0 ([`c1eb51b`](https://github.com/crccheck/django-object-actions/commit/c1eb51b96deb015e5fe481886c6f0f357655ebb3))

* Merge pull request #43 from Amareis/issue-42

Fix Django 1.9 compatibility, Drop Django 1.4 ([`04eb0d8`](https://github.com/crccheck/django-object-actions/commit/04eb0d88ce5e26cebf445902d6d0afffa7dfcc4b))

* Some decorative fixes ([`fd28613`](https://github.com/crccheck/django-object-actions/commit/fd28613627251dad7117a421eb47f2c9d23dd349))

* Removed Django 1.4 testing ([`ca168dc`](https://github.com/crccheck/django-object-actions/commit/ca168dccc6504bc2cd38f3eb7d098c4b6e307e03))

* Updated CI configs ([`b576ade`](https://github.com/crccheck/django-object-actions/commit/b576ade988aa4634a4dd94cdad1bce12d2c23780))

* Fixed absolute URL&#39;s on reverse calls ([`0113594`](https://github.com/crccheck/django-object-actions/commit/0113594d307f564e338ef856da20ed45170e8e7a))

* Update change_form.html ([`416cabf`](https://github.com/crccheck/django-object-actions/commit/416cabf670c9410ea035c612cf1937ad4a87828f))

* Update utils.py ([`abc053b`](https://github.com/crccheck/django-object-actions/commit/abc053b60a01a6568bfd2f0e7a9d646aa15288d1))

* Merge pull request #35 from crccheck/maintenance

Maintenance tweaks ([`fae7d93`](https://github.com/crccheck/django-object-actions/commit/fae7d9334529cc1cd71882ee8a424886430e9019))

* bump required yet again to stay fresh ([`e063d5d`](https://github.com/crccheck/django-object-actions/commit/e063d5d39b9f38f383440feb4605637a780b6afc))

* Merge remote-tracking branch &#39;origin/master&#39; into maintenance ([`815fd2e`](https://github.com/crccheck/django-object-actions/commit/815fd2ecf06cb77991cf449cda3aff42c1af7410))

* Merge pull request #39 from AlexRiina/master

Fix how queryset-ish wasn&#39;t queryset-ish enough ([`3d02a3e`](https://github.com/crccheck/django-object-actions/commit/3d02a3e28640dda948f9de8e8eca8632f96ec6dc))

* upgrade django-extensions so build passes ([`30d1db2`](https://github.com/crccheck/django-object-actions/commit/30d1db29db0feb1e0090b7164dede3b4b84eb6cd))

* add get_queryset as perferred alternative to _meta.model ([`dd730c3`](https://github.com/crccheck/django-object-actions/commit/dd730c3382592e7b893ead2d0644b95899318eba))

* use pk instead of QuerySetIsh

fix use model or concrete model ([`e7bf8e5`](https://github.com/crccheck/django-object-actions/commit/e7bf8e56c5bcc806790fa0d3e2bf8a73da1c6bd0))

* test update on second poll ([`9612bcc`](https://github.com/crccheck/django-object-actions/commit/9612bcc7573d8b0fc459ff4b8b122f2039debd8a))

* disable python3.5 in travisci ([`1fa6acb`](https://github.com/crccheck/django-object-actions/commit/1fa6acb90c1245160eb29c5e4ceebb46316098c5))

* expand coverage to python 3.5 ([`bb9666d`](https://github.com/crccheck/django-object-actions/commit/bb9666dbd6394cf2604777ca81134df133ce955e))

* update makefile style a bit ([`5db392e`](https://github.com/crccheck/django-object-actions/commit/5db392e2ac369e4b8dedbbb18245fbe480c9ade7))

* delete some more things in &#39;make clean&#39; ([`9abb96d`](https://github.com/crccheck/django-object-actions/commit/9abb96d8db7b672b0e22161545ab314e24797bb8))

* bump requirements to stay fresh ([`2067389`](https://github.com/crccheck/django-object-actions/commit/2067389d17693382f8f1a75d2864555d790315e2))

* Merge pull request #34 from dukebody/master

Raise original object action KeyError instead of wrapping it ([`ba358f7`](https://github.com/crccheck/django-object-actions/commit/ba358f71202772c68a2cd2dfc6ef1acccab3186e))

* Raise original object action KeyError instead of wrapping it in &#34;Tool does not exist&#34;. ([`0a130e1`](https://github.com/crccheck/django-object-actions/commit/0a130e1a076b74bbbd364ffa8cb4b1995f04a450))

* Merge pull request #32 from crccheck/maintenance

Maintenance tweaks ([`bff321f`](https://github.com/crccheck/django-object-actions/commit/bff321f2f60262f3474638225395f3230530fd08))

* add shoutout too Django Admin Row Actions ([`c3aa307`](https://github.com/crccheck/django-object-actions/commit/c3aa307e937a138386fb8408c555ed6137668fba))

* bump requirements to stay fresh ([`988de59`](https://github.com/crccheck/django-object-actions/commit/988de595f71a3442cd728d4c1be7b9f7aa0d573c))

* change test runner to use the latest stable version of django ([`ac7e9df`](https://github.com/crccheck/django-object-actions/commit/ac7e9dfcf05d403d999873596d26e1369caebfe5))

* update django 1.8 coverage to the latest version ([`413c52b`](https://github.com/crccheck/django-object-actions/commit/413c52b5c74c9791846369b15e13cb41dd30a865))

* bump django 1.8c1 coverage ([`8ba1450`](https://github.com/crccheck/django-object-actions/commit/8ba14504877481680916519d900fdfa78423788e))

* Merge pull request #31 from crccheck/dj18

Officially support django 1.8 ([`50966dd`](https://github.com/crccheck/django-object-actions/commit/50966dd3733390ebcfa876e86e33c7e4c24d7f3c))

* add coveralls badge ([`b7528c0`](https://github.com/crccheck/django-object-actions/commit/b7528c0e7f6fe89768d719c10bc6b58d296d8794))

* add coveralls support so I get a badge ([`3e111df`](https://github.com/crccheck/django-object-actions/commit/3e111df42e7a7809d044b3e80acc9370fc69ecde))

* refactor tox install to use generated environments ([`f2a4ea4`](https://github.com/crccheck/django-object-actions/commit/f2a4ea48386ae9d478f13a438232282e1ae304cb))

* Add Django 1.8 to list of tested versions ([`62b221e`](https://github.com/crccheck/django-object-actions/commit/62b221e7f165cc3abc3d891b1dfda3e9808a43b8))

## v0.5.1 (2014-11-27)

### Unknown

* bump version to v0.5.1 ([`a34b4e9`](https://github.com/crccheck/django-object-actions/commit/a34b4e952f437126440f593cdb6c0d5797e00187))

* Merge pull request #30 from texastribune/uuid-pks-n-stuffing

Uuid pks n stuffing ([`fecf547`](https://github.com/crccheck/django-object-actions/commit/fecf54775e1f83a2075dbce72c2c8623f7339e60))

* add an easier way to bump versions ([`ad68b8b`](https://github.com/crccheck/django-object-actions/commit/ad68b8bdfda0f5aaa9d407b524021da52385dbc4))

* move factories out from package since this has no models ([`d9bef16`](https://github.com/crccheck/django-object-actions/commit/d9bef16c639eee73463f89a1a022be2ee7c8ec5b))

* delete excess files when packaged

don&#39;t need example_project and tests when packaging. it&#39;d be nice, but
it&#39;s not practical. ([`9611eaa`](https://github.com/crccheck/django-object-actions/commit/9611eaa0446828885d2d8b0fbac3fa2799c6c93e))

* update the way the url pattern is defined for future-proofin&#39;

I thought I read that defining urls without url(...) was going away. ([`0b12fb3`](https://github.com/crccheck/django-object-actions/commit/0b12fb32f2b68dd9492d967ecf2b353eee8e6098))

* minor coding style tweaks ([`3e7bb2a`](https://github.com/crccheck/django-object-actions/commit/3e7bb2a93808b9d315f4a83bb4fb1bf76b958e70))

* fix how actions did not work on uuid pks ([`791e09a`](https://github.com/crccheck/django-object-actions/commit/791e09a354e5008fd20a6b0afb08751e4e5cd5f3))

* add a new model with a uuid pk for more test coverage ([`fdad91f`](https://github.com/crccheck/django-object-actions/commit/fdad91fd97e6978cb139b335edbb887c81a507bf))

* update requirements to be supafresh ([`87381d1`](https://github.com/crccheck/django-object-actions/commit/87381d16b2f700aec4a04e4871746ad278588802))

* Merge pull request #28 from texastribune/random-tweaks

Random tweaks ([`c6a3419`](https://github.com/crccheck/django-object-actions/commit/c6a3419721584f94f50c27e8d95c8cedfd1af032))

* add a tiny bit more test coverage ([`4b514e1`](https://github.com/crccheck/django-object-actions/commit/4b514e170d1c1dc75962277878409dd5f92ffeb7))

* add some more docs here in there as I try and remember what I wrote ([`0a27184`](https://github.com/crccheck/django-object-actions/commit/0a27184a7908cc6dae82b96e85307e79b7be5f13))

* refactor render_change_form context to map for readability

to me, it makes more sense to read map() instead of a list comprehension ([`4fb1e8a`](https://github.com/crccheck/django-object-actions/commit/4fb1e8ab08f2b2353fda9e06441502e87467cfdb))

* update database to be .db which is what I normally do nowadays

and pin developers to django 1.7 so the &#39;migrate&#39; command is available ([`0fe4393`](https://github.com/crccheck/django-object-actions/commit/0fe4393800e3811dcd5752217ef85c25e45bae5c))

* Merge pull request #22 from texastribune/refresh-dev

Refresh dev environment ([`220506a`](https://github.com/crccheck/django-object-actions/commit/220506aeb8484e8fcf1d827e852c2704e5d7cdb8))

* bump most requirements up for some reason ([`535aeaf`](https://github.com/crccheck/django-object-actions/commit/535aeafa4ce7a016db50a5f7c68bcf4f3bdc31b3))

* Merge remote-tracking branch &#39;origin/master&#39; into refresh-dev

Conflicts:
	Makefile ([`b98c03c`](https://github.com/crccheck/django-object-actions/commit/b98c03cd7da16039a13577a85352f272d53a0787))

* Merge pull request #26 from texastribune/dj17-and-testing-refresh

Django 1.7 and testing refresh ([`c446423`](https://github.com/crccheck/django-object-actions/commit/c4464230699cd774b291319a49d3a32c7cbc2662))

* remove nose as a requirement so project is simpler ([`1869129`](https://github.com/crccheck/django-object-actions/commit/18691294df33def882e542c36a825ee0f5052a9f))

* add coverage to the project ([`b4b1191`](https://github.com/crccheck/django-object-actions/commit/b4b11914cf5ea8d5e136d5ed7f0e85f152184e50))

* fix failing django 1.4 test setup ([`f1369aa`](https://github.com/crccheck/django-object-actions/commit/f1369aa3e2e334b45abc8fe49ae36278741e65e2))

* update django testing requirements to Django 1.7 ([`df48a1c`](https://github.com/crccheck/django-object-actions/commit/df48a1cedf2935318563e77dd783959d02d3ef13))

* remove dependency on django-nose ([`e15e211`](https://github.com/crccheck/django-object-actions/commit/e15e2117bb64c1fbbddeeea70a52c6181c6c2f4f))

* fix how django wanted pytz installed ([`b2d8226`](https://github.com/crccheck/django-object-actions/commit/b2d82268ba0157227d0b058dc97ca53273f95fd5))

* refresh readme documentation with simplifications/updates ([`6d7f9e9`](https://github.com/crccheck/django-object-actions/commit/6d7f9e92eff64c3fd56f28ba828468d286c46313))

* Merge pull request #20 from texastribune/django-17

Bump tox to test latest Django 1.7 ([`f347dd4`](https://github.com/crccheck/django-object-actions/commit/f347dd43ea320051df52200c5c640f4c16435328))

* doc when to delete this weird setting ([`ba6a44a`](https://github.com/crccheck/django-object-actions/commit/ba6a44a6554988cf845161968633a41ed9beb1b9))

* get all tox tests to pass again finally ([`a8ff753`](https://github.com/crccheck/django-object-actions/commit/a8ff753ca0cb121818af5b1188b063cab2e2aab9))

* shutup, factoryboy ([`d63a70e`](https://github.com/crccheck/django-object-actions/commit/d63a70e08f0233b7ce590709476675dd65f553e9))

* slowly migrate away from using fixtures ([`6bd056c`](https://github.com/crccheck/django-object-actions/commit/6bd056ce16a52bf36c65f97eb0b8949e9f36d51e))

* get test runner to shut up for stupid django 1.7 warnings ([`9e8b4c9`](https://github.com/crccheck/django-object-actions/commit/9e8b4c9f855402bf056717cca0dd9c13bcc47cc1))

* stfu, django ([`526e781`](https://github.com/crccheck/django-object-actions/commit/526e781468bfd7b237fe7fcacc73108e1e2f8060))

* simplify requirements and add factoryboy==2.4.1 ([`1b41c9b`](https://github.com/crccheck/django-object-actions/commit/1b41c9b33bfddd9335db9ef5becf4a0ed07f5b4c))

* bump django 1.7 to latest rc ([`ca2ecfc`](https://github.com/crccheck/django-object-actions/commit/ca2ecfc52c022ce4d1d7a98cdf70dc6b2f83b075))

* update setup.py to not package support for tests

thanks to info I found in
http://blog.schwuk.com/2014/03/19/using-tox-django-projects/ ([`d18dc70`](https://github.com/crccheck/django-object-actions/commit/d18dc70b664a317251750191d396fec1ed4f83b2))

* Merge pull request #19 from maestrofjp/master

Documented example of a custom get_object_actions() method ([`75f3111`](https://github.com/crccheck/django-object-actions/commit/75f3111bd7e549d3ce7da0a7a36d551857e9f6d5))

* Fixed typo

Blurg... fixed verb tense shift. ([`4faadde`](https://github.com/crccheck/django-object-actions/commit/4faaddee01272a68d2772292e98ab9ffa9edfe7f))

* Documented example of a custom get_object_actions() method

Includes note about that context[&#39;original&#39;] is not available when creating / adding new objects (and object actions can&#39;t be applied in that case anyways). ([`1f8ba57`](https://github.com/crccheck/django-object-actions/commit/1f8ba57989653bb181d52d67a7e1af0c3f6bacba))

## v0.5.0 (2014-07-01)

### Unknown

* bump to v0.5.0 ([`635778c`](https://github.com/crccheck/django-object-actions/commit/635778c6e43f681df858de5c8e0d3082a9e151b7))

* Revert &#34;bump django 1.7 test to release candidate 1&#34;

This reverts commit 9e56b89ce8e0f526bd956bcc21fcb3b77b2a2c09.

ugh ([`29d05ac`](https://github.com/crccheck/django-object-actions/commit/29d05ac23a3f8c00e50a6bdc92a9532e5cf6b15e))

* bump django 1.7 test to release candidate 1 ([`9e56b89`](https://github.com/crccheck/django-object-actions/commit/9e56b89ce8e0f526bd956bcc21fcb3b77b2a2c09))

* Merge pull request #15 from texastribune/bleeding-edge

Extend to Django 1.7b1 and Python 3.4 ([`2e15ba2`](https://github.com/crccheck/django-object-actions/commit/2e15ba2ac5514ea1d13c7357f4018ee1f8609c55))

* bump to latest django 1.7 beta ([`e2b955c`](https://github.com/crccheck/django-object-actions/commit/e2b955c17df09fbfa40d7c93c34853e2ba287a22))

* add failing test case for filtering a fake queryset

this could be fixed by undoing the `get` method hack, but is it even
needed? ([`f758851`](https://github.com/crccheck/django-object-actions/commit/f7588519d9581ba3762a8a4ab7d64e66ac033d8a))

* add tests to make sure other queryset methods work ([`9118f73`](https://github.com/crccheck/django-object-actions/commit/9118f73f02723bcf62c82934f3ea36328777da25))

* oops, forgot travisci stuff ([`10504d4`](https://github.com/crccheck/django-object-actions/commit/10504d4e9546853f28783e6120a950164ffbd485))

* add python 3.4 to tox ([`222b754`](https://github.com/crccheck/django-object-actions/commit/222b754719acba2caeaaab1ca9406425c0db53a8))

* upgrade tox==1.7.1 ([`bd98b03`](https://github.com/crccheck/django-object-actions/commit/bd98b031eb3956ad27d0bf6717af75de5b60d556))

* fix .get() stopped working in django 1.7 ([`8f1a9fc`](https://github.com/crccheck/django-object-actions/commit/8f1a9fc58aaace41fe71b80838ceaa63bf1dac44))

* update tox to do django1.7b1 ([`a5c4fcc`](https://github.com/crccheck/django-object-actions/commit/a5c4fcc2cd5576a5600de1ee53bb3338c10cabfd))

* Merge new &#39;get_object_actions()&#39; function ([`a212beb`](https://github.com/crccheck/django-object-actions/commit/a212beba63431510e56fedfbdda9e4591fa1f10e))

* add a test to verify how get_object_actions works ([`c726838`](https://github.com/crccheck/django-object-actions/commit/c726838deb51e139ecb441bc5d0a5ec49ed270d1))

* whitespace ([`ca952da`](https://github.com/crccheck/django-object-actions/commit/ca952da4ec832b3f48a644ea19d140ec1672b3fd))

* Added get_object_actions() function

Can use context[&#39;original&#39;] (the model) to return dynamic objectactions. Note that this won&#39;t affect the url setup -- modeladmin.objectactions should include all possible actions. ([`b50e350`](https://github.com/crccheck/django-object-actions/commit/b50e350b688996958606328f6e8a2362b7dffccf))

## v0.4.0 (2014-02-12)

### Unknown

* bump version to v0.4.0 ([`8909177`](https://github.com/crccheck/django-object-actions/commit/8909177a97f792fd24348b29033cd739ef6a852e))

* Merge pull request #13 from texastribune/attrs-everywhere

Add ability to set arbitrary attributes on the buttons ([`61e73c2`](https://github.com/crccheck/django-object-actions/commit/61e73c293508e949a294f0b5e43f8df4d485e8ed))

* add documentation of .attrs attr ([`9d38714`](https://github.com/crccheck/django-object-actions/commit/9d38714c51d72c84d6ea1bdc4877339cb03643c1))

* make sure it renders attrs escaped ([`6d798d5`](https://github.com/crccheck/django-object-actions/commit/6d798d5d29b27aff1ac582ee149ea38a2c2c98b5))

* add: incorporate custom attrs into the template ([`4d9e3fa`](https://github.com/crccheck/django-object-actions/commit/4d9e3fa999cdf5dc5d9a8bc08b3d5f5eef295434))

* update to disallow custom title attr ([`29bfd95`](https://github.com/crccheck/django-object-actions/commit/29bfd9530b9eea535947e66b16263968b323caac))

* 1am coding does this ([`f072415`](https://github.com/crccheck/django-object-actions/commit/f0724151590262102086f23c6b3aba8d20060ce5))

* make sure custom attrs are partitioned off ([`5b3662a`](https://github.com/crccheck/django-object-actions/commit/5b3662a31b2ad0574aeef53d646267cc0c496030))

* make sure &#39;href&#39; isn&#39;t allowed to be set ([`47d78b8`](https://github.com/crccheck/django-object-actions/commit/47d78b88d4a5762a71bf823582a742a22e7a7408))

* convert short_description to a title attr and add class ([`25831b2`](https://github.com/crccheck/django-object-actions/commit/25831b26ef15ee1cf9497d8438b3e1fe4e1a5810))

* add a way to get a new &#39;attrs&#39; attribute into the template ([`0894887`](https://github.com/crccheck/django-object-actions/commit/0894887d8781a9df9b2ed04a6e0e7ed494866d87))

* add: linkify travisci badge ([`a46a311`](https://github.com/crccheck/django-object-actions/commit/a46a311bfb6168b3a61fec683965bcabd4c19a35))

* tweak the description for this package ([`f4b2076`](https://github.com/crccheck/django-object-actions/commit/f4b2076eae9c2d7049f11881078797374f375649))

## v0.3.0 (2014-01-09)

### Unknown

* bump version to v0.3.0

fixes a scope bug
increases test coverage
adds another way to integrate ([`c184d76`](https://github.com/crccheck/django-object-actions/commit/c184d763af817695d281db3e051f3b04996ec236))

* Merge pull request #10 from crccheck/better-naked

Add a way to opt out of template helpers ([`402fc66`](https://github.com/crccheck/django-object-actions/commit/402fc66ca57cbab5222fe8671660965195ad8de3))

* rewrite readme for new usage and for clarity ([`4a94c1e`](https://github.com/crccheck/django-object-actions/commit/4a94c1e165c9cb51e636d25e36fde027492da9a0))

* move change_form_template attr out ([`7b25ff8`](https://github.com/crccheck/django-object-actions/commit/7b25ff81b76dffc38702fdae619ddf1ad478f8fc))

* Merge pull request #9 from crccheck/matrix

Increase testing coverage ([`8e5d462`](https://github.com/crccheck/django-object-actions/commit/8e5d462fbf21ae6a2a54d67fe34ee64bdace5ef7))

* add testing coverage across python 2.6 to python 3.3 ([`8d35b57`](https://github.com/crccheck/django-object-actions/commit/8d35b5739618083df0a215a03bd10612fe2b040f))

* fix wrong variable name was used

luckily, variable scoping keeps it from breaking until python 3.3 ([`e1a836a`](https://github.com/crccheck/django-object-actions/commit/e1a836a5f0bf45854ae634134984a69517c4c1e0))

* change pypi classifier to &#39;beta&#39; ([`99c46ba`](https://github.com/crccheck/django-object-actions/commit/99c46ba19522e853f097c5fddba671a2acc68626))

## v0.2.0 (2013-11-09)

### Unknown

* bump version to v0.2.0 ([`5fe0184`](https://github.com/crccheck/django-object-actions/commit/5fe01845b85345e81ac8eca918c736223b3700f8))

* Merge pull request #5 from crccheck/double-duty

Allow regular actions written for the admin to also work for this package ([`105dc0a`](https://github.com/crccheck/django-object-actions/commit/105dc0a9404a7f00a684a9c308a31e0a2dd6ac3d))

* tweak format of limitations section of readme ([`5acd9d7`](https://github.com/crccheck/django-object-actions/commit/5acd9d7eedb303c49104b1c0410cbc01d2da590d))

* add docs for takes_instance_or_queryset ([`820a216`](https://github.com/crccheck/django-object-actions/commit/820a2161cc7321d009103ab0dd2b32a06f7e9642))

* use the decorator in the example project

also fix typos in the short descriptions ([`35df010`](https://github.com/crccheck/django-object-actions/commit/35df010376ec0b3e39b565a5c6911c8db0005451))

* fix django 1.5 is special in how you get the model

fixes the error:

    AttributeError: &#39;Options&#39; object has no attribute &#39;model&#39; ([`e6b5efb`](https://github.com/crccheck/django-object-actions/commit/e6b5efb6236caf8ebb5960129b7ae0e81933080b))

* add decorator so actions work on objects or querysets ([`9af42e1`](https://github.com/crccheck/django-object-actions/commit/9af42e11cd6952cb3c5df9c48ffc0f9857f656f6))

* add util for turning an instance back into a queryset ([`eaefa64`](https://github.com/crccheck/django-object-actions/commit/eaefa64fd0adbca110a6cc74ba8ad9b0fb48cd27))

* add .env to gitignore ([`733efcb`](https://github.com/crccheck/django-object-actions/commit/733efcb06642dc8457d678fc3c300df495f346bc))

* update docstring styles ([`e46a1a0`](https://github.com/crccheck/django-object-actions/commit/e46a1a0f223989dd7cdb1582a1f917da23122b9a))

* Merge pull request #4 from crccheck/testing-refresh

Update testing strategy to use tox ([`19aede0`](https://github.com/crccheck/django-object-actions/commit/19aede0a16fd1f518f934a1c6b499e1519673e6d))

* add django16 coverage to tox ([`51274f2`](https://github.com/crccheck/django-object-actions/commit/51274f28da55cb9109ab96400a4444b25e7b2321))

* try tox + travis

This was the best reference I could find on how to do this:
https://github.com/datastax/python-driver/pull/26/files ([`bd445b4`](https://github.com/crccheck/django-object-actions/commit/bd445b48051c9e4bcf23b14fc571e15f97ccce7e))

* silence warning about django urls import ([`037a3e5`](https://github.com/crccheck/django-object-actions/commit/037a3e5f8b8db8547c269ae067a0967849be0d52))

* move tests under package ([`e261f15`](https://github.com/crccheck/django-object-actions/commit/e261f150a85094c96cdc1634ccf36a9cee1f4c77))

* simplify example_project a bit ([`cd4d3ff`](https://github.com/crccheck/django-object-actions/commit/cd4d3fff48229ea173a74bbc69fcda0a963af5df))

* test against django 1.4 and django 1.5 ([`2bb4a87`](https://github.com/crccheck/django-object-actions/commit/2bb4a87e67bc0c4bbb19558fa858468ff3591c40))

* hack in basic tox support ([`ee5777d`](https://github.com/crccheck/django-object-actions/commit/ee5777d638b360169af0d075febd9cc3aaea82fc))

* update installation instructions, is pip installable ([`12d7dc6`](https://github.com/crccheck/django-object-actions/commit/12d7dc637bfd9993ae11a9e27c04df0e4551a9db))

* Merge pull request #3 from lionheart/master

Fix broken import on Django 1.6 ([`a4ee597`](https://github.com/crccheck/django-object-actions/commit/a4ee59714e6d69f55fc50e759045b1d9c8f21e9b))

* fix broken import on Django 1.6

django.conf.urls.defaults is no longer a valid module. ([`4818175`](https://github.com/crccheck/django-object-actions/commit/4818175b9d99b86308cad0041573a48a8bb84f21))

## v0.1.1 (2013-02-26)

### Unknown

* bump version to 0.1.1 ([`0e4f65e`](https://github.com/crccheck/django-object-actions/commit/0e4f65e6da65d155059878cd8034aac83f25ef61))

* add a url attr to setup ([`587a3d1`](https://github.com/crccheck/django-object-actions/commit/587a3d1fdb763e654dc226979fe7ab6c71e17a4b))

* convert readme to restructured text

thank you, pandoc! ([`1e5a610`](https://github.com/crccheck/django-object-actions/commit/1e5a6101bc2f844f3641caa003ab354cdb4db566))

## v0.1.0 (2013-02-24)

### Fix

* fix: make sure not to include pyc files ([`d52f802`](https://github.com/crccheck/django-object-actions/commit/d52f8020024499df7e0bec6f7606707e9045b90b))

* fix: actions showed up in /add/, they shouldn&#39;t ([`bd23a60`](https://github.com/crccheck/django-object-actions/commit/bd23a6023b3358d6ec0a59b50774d1f5d5d422ed))

### Unknown

* version bump to v0.1.0 ([`7f20d1f`](https://github.com/crccheck/django-object-actions/commit/7f20d1f328a18ba6ac6c4535d0e9f7b40227fc8f))

* update LICENSE file to use full license text ([`37b2717`](https://github.com/crccheck/django-object-actions/commit/37b27179f0384ee31396c244621c48d096925fe3))

* add a test to demo we can get a template out of a tool ([`20d42f9`](https://github.com/crccheck/django-object-actions/commit/20d42f9e37582be5f248ac4230030bdca8af568a))

* add test to make sure we can return a template ([`81f742c`](https://github.com/crccheck/django-object-actions/commit/81f742c47f4374243bdbcb4a07470c81ec45c7b9))

* add test for a tool with an intermediate/POST ([`41ca626`](https://github.com/crccheck/django-object-actions/commit/41ca62642e3ec124071d505b30e741f42df2b26f))

* Merge remote-tracking branch &#39;jimfunk/master&#39; into post ([`13431b0`](https://github.com/crccheck/django-object-actions/commit/13431b0d73a14383443e1bcbc56e93667f3a0663))

* Allow POST requests ([`83fbce6`](https://github.com/crccheck/django-object-actions/commit/83fbce6326f8f7bfcc8e3c81509e81b24d59c8e9))

* begin adding example of making a tool with an intermediate page ([`fd26c94`](https://github.com/crccheck/django-object-actions/commit/fd26c94cae97c641e4d5d10374521e65a235b58b))

* oops, use just the path for the url to test ([`7df4ee9`](https://github.com/crccheck/django-object-actions/commit/7df4ee940294c057df016b300fdc136164c7fb7f))

* update make help formatting ([`159c8e6`](https://github.com/crccheck/django-object-actions/commit/159c8e62f2ea3b8e30dd7ba2858607ee883a055c))

* add travis-ci bug to readme ([`5ae476c`](https://github.com/crccheck/django-object-actions/commit/5ae476c8775dc6fdfa9138f6a9781f029d3daf2a))

* update: ignore build/ directory ([`91faec2`](https://github.com/crccheck/django-object-actions/commit/91faec21afad541745eff080a5fabd07108f7e4c))

* switch to django-extension&#39;s reset_db

this allows development in sqlite, mysql, and postgresql ([`a5bf8b5`](https://github.com/crccheck/django-object-actions/commit/a5bf8b5f35164e13f85c39f3843d5084a95fd1f1))

* enable django-extensions ([`f312e6d`](https://github.com/crccheck/django-object-actions/commit/f312e6d78006b9c8c8a33ccae381bf16d1c882a6))

* update readme with more stuffffffsssss ([`5625d9e`](https://github.com/crccheck/django-object-actions/commit/5625d9e05d27cbd6ce03194fdeb447b27a85484c))

* add a travis-ci support ([`4b61d5d`](https://github.com/crccheck/django-object-actions/commit/4b61d5dd03c212ded945a07ae36617809f27bf1f))

* add &#39;make clean&#39; to remove distutils generated files ([`aaab73d`](https://github.com/crccheck/django-object-actions/commit/aaab73d1f3e0f7734bfd62a4be2f815dd994d6db))

* Merge branch &#39;random-updates&#39; ([`54b7c6a`](https://github.com/crccheck/django-object-actions/commit/54b7c6a9468b94a575f526794099b410cd34b73a))

* move docs to readme ([`d818495`](https://github.com/crccheck/django-object-actions/commit/d818495bf2ad7f120ed63039289eea32cac62058))

* add the tool name as a data attr

make it easier to target with css or js ([`0e6acb8`](https://github.com/crccheck/django-object-actions/commit/0e6acb82b0d2adbdcd2aa7fe5b85b3efad970240))

* add a label property to customize the button label ([`4e83c00`](https://github.com/crccheck/django-object-actions/commit/4e83c003aa694168db421a1eb6436de5bcc7c633))

* refactor the way tools are passed into the context ([`14fe260`](https://github.com/crccheck/django-object-actions/commit/14fe260d1e3c5e8fdbc82c2a7e61f659fde99667))

* set the version to a non-zero minor version: 0.1.0-dev ([`c5fe5b9`](https://github.com/crccheck/django-object-actions/commit/c5fe5b93c81eb17600fd6eac43583f2829c38d98))

* throw on some more setup.py pypi classifiers ([`95d1f63`](https://github.com/crccheck/django-object-actions/commit/95d1f63ce4d9698f8ab4b64757e3669c75accbbd))

* refactor setup.py: using find_packages is excessive ([`6b3c277`](https://github.com/crccheck/django-object-actions/commit/6b3c277b3d7eb673c1f757796c63b4695aa43b0a))

* update package authorship info to a texastribune.org email ([`b72d5d8`](https://github.com/crccheck/django-object-actions/commit/b72d5d89f377f5fec8076675e2d6d4e5dc61408c))

* Merge pull request #1 from jimfunk/master

Don&#39;t pull metadata from the application ([`c8c7c78`](https://github.com/crccheck/django-object-actions/commit/c8c7c78a1ab4943e82e41c7ad339701aa49c545a))

* Don&#39;t pull metadata from the application

It imports Django modules that require the settings module, which breaks
installation. ([`bb65333`](https://github.com/crccheck/django-object-actions/commit/bb653333a6e15a9d4efe56c457f4331fdd484c3c))

* add a test to make sure tools functions actually get called ([`892a838`](https://github.com/crccheck/django-object-actions/commit/892a838d6a6b25e6cae6a4f8527c3912767623a5))

* add: tools can now return httpresponse objects ([`e20748d`](https://github.com/crccheck/django-object-actions/commit/e20748d16f14671146b61378aa1e1dff63995f9d))

* update: kill hacks. oh wait, found found the right block name ([`b589718`](https://github.com/crccheck/django-object-actions/commit/b589718c476600c890ad1b237d1c44a00fe864eb))

* add help command to phony make targets ([`b18b20e`](https://github.com/crccheck/django-object-actions/commit/b18b20e9850eb9ab23587f63ac40b7a96b74330e))

* add documentation to main utils ([`efce114`](https://github.com/crccheck/django-object-actions/commit/efce114e6baa2d8f0f4d473276247ead799ea349))

* add preliminary tests ([`ff84fc2`](https://github.com/crccheck/django-object-actions/commit/ff84fc27c7a8a5f93ffd971fbc8ca26479d31c32))

* update setup.py meta-data ([`1cd14a7`](https://github.com/crccheck/django-object-actions/commit/1cd14a7037c62d68f55175ac16a0a17e96edd59c))

* add more actions! ([`557b204`](https://github.com/crccheck/django-object-actions/commit/557b204240a7a1fab501a08846fecb6fe09ffcf1))

* clean up the javascript hack to move the list items ([`deaf2e0`](https://github.com/crccheck/django-object-actions/commit/deaf2e0a796e6a45a375949b5d4b0cd73e9e678d))

* add object actions to a new choice admin, hack stuff to make it work ([`16f220e`](https://github.com/crccheck/django-object-actions/commit/16f220e63cf36a94a4c792bbc5945a87bd97d512))

* add example polls app

I wonder where I got it from ([`f3a4ffa`](https://github.com/crccheck/django-object-actions/commit/f3a4ffa90f277ac572af1de80e353de857b01820))

* add an initial fixture with superuser admin/admin ([`2ae4284`](https://github.com/crccheck/django-object-actions/commit/2ae4284378a48380c3cffd7ad2221a884381e5ac))

* add gitignore

Apparently cp -r does not grab hidden files
remove accidentally commited files ([`c39994b`](https://github.com/crccheck/django-object-actions/commit/c39994bd44374015d2ae2dc64dbe0a778a035008))

* rename things around

I&#39;ll probably have to do this again, but gotta start somewhere. ([`ebb3db3`](https://github.com/crccheck/django-object-actions/commit/ebb3db34a474c8ac502226a5fa5f29c1de3e3121))

* copy in existing code from another project and wire it up ([`01afb91`](https://github.com/crccheck/django-object-actions/commit/01afb912ee3e6a991e9aed560f7c7cbe980a7c01))

* add django-admin startapp skeleton ([`d1aa83b`](https://github.com/crccheck/django-object-actions/commit/d1aa83b2393e1aa196df4901620eb0aa07b136a7))

* initial commit ([`a8acd8e`](https://github.com/crccheck/django-object-actions/commit/a8acd8eacc9712c133886651d99f5c5794cd4592))
