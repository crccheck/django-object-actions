from distutils.core import setup


setup(
    name='django-object-actions',
    version='0.0.1',
    author="The Texas Tribune",
    author_email="cchang@texastribune.org",
    maintainer="Chris Chang",
    # url
    packages=['django_object_actions'],
    include_package_data=True,  # automatically include things from MANIFEST
    license='Apache License, Version 2.0',
    description='A Django app for adding object tools to models',
    long_description=open('README.md').read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
    ],
)
