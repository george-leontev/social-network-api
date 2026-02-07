from abc import ABC
from typing import Any
from datetime import datetime
from pydantic import BaseModel, field_validator

from utils.strings import snake_to_camel


class AppBaseModel(ABC, BaseModel):
    """
    The most common abstract model inherited from the pydantic base model.
    It defines custom serialization rules throughout this project
    """

    class Config:
        alias_generator = snake_to_camel
        allow_population_by_field_name = True
        validate_by_name = True
        ensure_ascii = False
        json_encoders = {
            datetime: lambda v: v.strftime("%Y-%m-%dT%H:%M:%SZ"),
            float: lambda x: round(x, 2),
        }

    @field_validator("*", mode="before")
    @classmethod
    def round_floats(cls, value: Any) -> Any:
        if isinstance(value, float):
            return round(value, 2)
        return value
