FROM python:2-onbuild

ARG DJANGO_VERSION

RUN pip install django==$DJANGO_VERSION

ENV PORT 8000
EXPOSE 8000

ENV PYTHONPATH /usr/src/app

RUN make resetdb
RUN echo "from django.contrib.auth import get_user_model; \
  User = get_user_model(); \
  User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | \
  python example_project/manage.py shell

CMD python example_project/manage.py runserver 0.0.0.0:$PORT
