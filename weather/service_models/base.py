"""Base Service Model for all the models."""

from humps import camelize
from pydantic import BaseModel


def to_camel(string: str) -> str:
    return camelize(string)


class BaseCamelModel(BaseModel):
    """
    A base model that converts all dict keys to camel case.

    This is used in the service models to convert
    the dict keys to camel case and vice versa.
    """

    class Config:
        alias_generator = to_camel
        populate_by_name = True
