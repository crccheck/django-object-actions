from setuptools import setup


setup(
    name='django-object-actions',
    version='0.1.1',
    author="The Texas Tribune",
    author_email="cchang@texastribune.org",
    maintainer="Chris Chang",
    url="https://github.com/texastribune/django-object-actions",
    packages=['django_object_actions'],
    include_package_data=True,  # automatically include things from MANIFEST
    license='Apache License, Version 2.0',
    description='A Django app for adding object tools to models',
    long_description=open('README.rst').read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
    ],
)
