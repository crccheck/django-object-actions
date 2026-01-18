FROM python:3.12-alpine

RUN apk add --no-cache make

ADD . /app
WORKDIR /app
ENV PYTHONPATH=/app

RUN pip --disable-pip-version-check install -e '.[dev]'

RUN make resetdb
RUN echo "from django.contrib.auth import get_user_model; \
  User = get_user_model(); \
  User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | \
  python example_project/manage.py shell

ENV PORT=8000
EXPOSE 8000

CMD ["python", "example_project/manage.py", "runserver", "0.0.0.0:8000"]
