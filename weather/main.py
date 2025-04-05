"""The entrypoint into the FastAPI-based server."""
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers import weather 
from settings.utils import get_environment

APP_NAME = "Weather API"
VERSION = "0.0.1"
env: str = get_environment()
app = FastAPI(title=APP_NAME, version=VERSION)


app.include_router(weather.router, prefix="", tags=["Weather"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port="8010")
