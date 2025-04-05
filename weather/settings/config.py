import os
from pathlib import Path

import yaml


class Config:
    def __init__(self):
        env = os.getenv("APP_ENV", "local").lower()
        config_filename = f"{env}.yaml"

        # Get the root directory (2 levels up from this file)
        base_dir = Path(__file__).resolve().parents[2]
        config_path = base_dir / config_filename

        if not config_path.exists():
            raise FileNotFoundError(f"Configuration file '{config_path}' not found.")

        with open(config_path) as file:
            self.config = yaml.safe_load(file)

    def get_weather_config(self):
        return self.config.get("weather_api", {})
