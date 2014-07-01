from setuptools import setup


setup(
    name='django-object-actions',
    # hey, remember to update __version__ too
    version='0.5.0',
    author="The Texas Tribune",
    author_email="cchang@texastribune.org",
    maintainer="Chris Chang",
    maintainer_email='c@crccheck.com',
    url="https://github.com/texastribune/django-object-actions",
    packages=[
        'django_object_actions',
        # The following packages are only here to support testing.
        'django_object_actions.tests',
        'example_project',
    ],
    include_package_data=True,  # automatically include things from MANIFEST
    license='Apache License, Version 2.0',
    description='A Django app for adding object tools for models in the admin',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
