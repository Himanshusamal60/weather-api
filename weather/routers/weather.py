import requests
from fastapi import APIRouter, HTTPException, Response
from service_models.weather import WeatherRequest, WeatherResponse
from services import WeatherService
from settings.utils import convert_to_xml

router = APIRouter()
weather_service = WeatherService()


@router.post("/getCurrentWeather", response_model=WeatherResponse)
async def get_current_weather(request: WeatherRequest) -> WeatherResponse | Response:
    city = request.city
    output_format = request.output_format.lower()

    if output_format not in {"json", "xml"}:
        raise HTTPException(status_code=400, detail="Invalid output_format. Use 'json' or 'xml'.")

    try:
        weather_data = weather_service.get_weather(city)

        if output_format == "json":
            return WeatherResponse(**weather_data)

        xml = convert_to_xml(weather_data)
        return Response(content=xml, media_type="application/xml")

    except requests.RequestException as e:
        raise HTTPException(status_code=503, detail="Weather service is currently unavailable.") from e

    except ValueError as e:
        raise HTTPException(status_code=422, detail="Invalid response data.") from e

    except Exception as e:
        raise HTTPException(status_code=400, detail="Unexpected error occurred.") from e
