FROM python:3.11-slim-bookworm

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1

# Set the configuration setting
ARG APP_ENV=dev
ENV APP_ENV=$APP_ENV


WORKDIR /weather

RUN pip install pipenv

COPY ./Pipfile* ./

RUN pipenv install --system --deploy

COPY ./ ./

EXPOSE 8000

WORKDIR /weather/weather/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
