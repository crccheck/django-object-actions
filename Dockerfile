FROM python:2-onbuild

ARG DJANGO_VERSION

RUN pip install django==$DJANGO_VERSION

ENV PORT 8000
EXPOSE 8000

ENV PYTHONPATH /usr/src/app

CMD python example_project/manage.py runserver 0.0.0.0:$PORT
