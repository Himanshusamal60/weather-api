"""Utility functions required for the application."""

import os
from pathlib import Path
import xml.etree.ElementTree as ET



def get_environment() -> str:
    """Get the environment from the system variable."""
    environment = os.getenv("APP_ENV", "dev").lower()
    ALLOWED = {"local", "local-docker", "dev", "test", "stage", "prod"}
    if environment not in ALLOWED:
        raise Exception(
            "A proper configuration was not found in `APP_ENV` system variable. "
            f"The allowed values are either of {ALLOWED}, "
            f"but got `{environment}` instead.",
        )
    return environment



def convert_to_xml(data: dict) -> str:
    root = ET.Element("root")

    for key, value in data.items():
        element = ET.SubElement(root, key.replace(" ", ""))
        element.text = str(value)

    return ET.tostring(root, encoding="utf-8", method="xml").decode()