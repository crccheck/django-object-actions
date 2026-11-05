FROM python:3.15-alpine

RUN apk add --no-cache make

ADD . /app
WORKDIR /app
ENV PYTHONPATH=/app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
RUN uv pip install --system -e . --group dev

RUN make resetdb
RUN echo "from django.contrib.auth import get_user_model; \
  User = get_user_model(); \
  User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | \
  python example_project/manage.py shell

ENV PORT=8000
EXPOSE 8000

CMD ["python", "example_project/manage.py", "runserver", "0.0.0.0:8000"]
