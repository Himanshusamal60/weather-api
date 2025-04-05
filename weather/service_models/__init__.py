# ruff: noqa
"""Define all service models."""

from service_models.weather import WeatherRequest, WeatherResponse


__all__ = [
    "WeatherRequest",
    "WeatherResponse",
]
