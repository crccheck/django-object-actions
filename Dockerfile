# TODO upgrade once old Django versions are dropped
FROM python:3.9-alpine

RUN apk add --no-cache make

ADD requirements.txt /app/requirements.txt
RUN pip --disable-pip-version-check install -r /app/requirements.txt

ARG DJANGO_VERSION
RUN pip --disable-pip-version-check install django==$DJANGO_VERSION

ADD . /app
WORKDIR /app
ENV PYTHONPATH /app

RUN make resetdb
RUN echo "from django.contrib.auth import get_user_model; \
  User = get_user_model(); \
  User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | \
  python example_project/manage.py shell

ENV PORT 8000
EXPOSE 8000

CMD python example_project/manage.py runserver 0.0.0.0:$PORT
