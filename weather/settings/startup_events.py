"""Events to run during the starting of the application."""

from functools import lru_cache
from pathlib import Path

import yaml

from settings.config import AppConfig
from settings.utils import get_environment

environment = get_environment()
project_directory = Path(__file__).resolve().parents[2]
CONFIG_FILE_PATH = project_directory / f"{environment}.yaml"

CONFIG: AppConfig


@lru_cache
def load_config_file() -> None:
    """Load the YAML configuration file."""
    global CONFIG

    try:
        with open(CONFIG_FILE_PATH) as file:
            config_ = yaml.safe_load(file)
    except FileNotFoundError:
        raise Exception(
            f"{environment}.YAML file not found at {CONFIG_FILE_PATH}",
        ) from None
    except yaml.YAMLError as e:
        raise Exception(f"Error parsing the {environment}.YAML file: {e}") from e
    except Exception as e:
        raise Exception(f"Error DuringReading The {environment}.YAML File: {e}") from e

    CONFIG = AppConfig(**config_)


load_config_file()
