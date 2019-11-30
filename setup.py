from setuptools import setup


setup(
    name="django-object-actions",
    version="2.0.0",
    author="Chris Chang",
    author_email="c@crccheck.com",
    url="https://github.com/crccheck/django-object-actions",
    packages=["django_object_actions"],
    include_package_data=True,  # automatically include things from MANIFEST
    license="Apache License, Version 2.0",
    description="A Django app for adding object tools for models in the admin",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
