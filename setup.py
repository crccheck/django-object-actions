from setuptools import find_packages
from distutils.core import setup

import django_object_actions

setup(
    name='INSERT NAME HERE',
    version=django_object_actions.__version__,
    # author
    # author_email
    # url
    packages=find_packages('.', exclude=('example_project*',)),
    include_package_data=True,  # automatically include things from MANIFEST
    license='Apache License, Version 2.0',
    long_description=open('README.md').read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
    ],
)
