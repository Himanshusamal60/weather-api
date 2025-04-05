from enum import Enum

from pydantic import BaseModel, Field

from service_models.base import BaseCamelModel


class OutputFormat(str, Enum):
    json = "json"
    xml = "xml"


class WeatherRequest(BaseModel):
    city: str = Field(..., example="pune")
    output_format: OutputFormat = Field(..., example="json")

class WeatherResponse(BaseCamelModel):
    weather: str = Field(..., example="37.0 C", description="Current temperature in Celsius")
    latitude: str = Field(..., example="18.5333", description="Latitude of the city")
    longitude: str = Field(..., example="73.8667", description="Longitude of the city")
    city: str = Field(..., example="Pune India", description="Formatted city and country name")
