#Weather API System

This FastAPI-based Weather API System provides current weather data (temperature, latitude, longitude, and city) for a given city, with support for JSON or XML output formats.

Executive Summary / Usage of the Project

This project exposes a single API endpoint:

POST /getCurrentWeather

Request Body:

{
  "city": "Pune",
  "output_format": "json"
}

Response (JSON):

{
  "weather": "37.0 C",
  "latitude": "18.5333",
  "longitude": "73.8667",
  "city": "Pune India"
}

Response (XML):

<?xml version="1.0" encoding="UTF-8" ?>
<root>
  <Temperature>37.0</Temperature>
  <City>Pune India</City>
  <Latitude>18.5333</Latitude>
  <Longitude>73.8667</Longitude>
</root>

This project is powered by a free tier of the Weather API via RapidAPI. Please avoid committing secrets like API keys to source control.

Setup

##Prerequisites👇

Python 3.11

Docker (for deployment)

OS: Windows / macOS / Linux

pip, git, and pipenv

Setup the Project

git clone <your-repo-url>
cd weather-api-system
pip install pipenv
pipenv install --dev
pipenv shell

##Project Structure

weather-api-system/
├── main.py                # Entry point
├── weather/
│   ├── router/
│   │   └── weather.py     # API Router
│   ├── services/
│   │   └── weather.py     # WeatherService class
│   └── service_models/
│       ├── request.py     # Request Pydantic model
│       └── response.py    # Response Pydantic model
├── settings/
│   ├── config.py          # Config loader based on APP_ENV (dev/local)
│   └── utils.py           # JSON → XML converter
├── dev.yaml               # Dev environment config
├── local.yaml             # Local environment config
├── Dockerfile             # Docker image builder
└── .pre-commit-config.yaml

Environment Configuration

Set the APP_ENV to select configuration file:

APP_ENV=local    # Uses local.yaml
APP_ENV=dev      # Uses dev.yaml

Update your launch.json or .env to include:

APP_ENV=local

Docker Deployment

✅ Local Build & Run

docker build -t fastapi-weather-app .
docker run -dp 8000:8000 --env APP_ENV=local fastapi-weather-app

✅ Dev / Prod Deployment

docker build -t fastapi-weather-app-dev .
docker run -dp 8000:8000 --env APP_ENV=dev fastapi-weather-app-dev

Free Deployment Options 🌍

Option 1: Deploy on Render

Create an account at https://render.com

Create a new Web Service

Set build command: pip install pipenv && pipenv install

Set start command: uvicorn main:app --host 0.0.0.0 --port 8000

Add environment variable: APP_ENV=dev

Expose port 8000

Option 2: Deploy on Railway

Login at https://railway.app

Connect GitHub repo

Use default Dockerfile

Add environment variable: APP_ENV=dev

Deploy

Option 3: Deploy on Fly.io

flyctl launch
flyctl secrets set APP_ENV=dev
flyctl deploy

Testing the API

Use Postman, cURL, or Swagger UI:

Swagger docs: http://localhost:8000/docs

Example cURL:

curl -X POST http://localhost:8000/getCurrentWeather \
  -H "Content-Type: application/json" \
  -d '{"city": "Pune", "output_format": "json"}'

Contributors

👨‍💻 Himanshu!
