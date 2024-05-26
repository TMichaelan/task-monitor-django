# Builder image
FROM python:3.12 as builder

WORKDIR /usr/src/app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt ./
RUN pip install -r requirements.txt

# Production
FROM python:3.12-slim as base

WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq5 \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd app \
  && useradd --create-home -g app app

COPY --from=builder /opt/venv /opt/venv
COPY . .

USER app

ENV PATH="/opt/venv/bin:$PATH"

EXPOSE 8000

CMD ["daphne", "-b", "0.0.0.0", "task_monitor.asgi:application"]


# Development
FROM base as dev

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc python3-dev postgresql-client procps \
    && rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.dev.txt

USER app