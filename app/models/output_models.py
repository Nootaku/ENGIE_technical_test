"""OUTPUT MODELS

This file contains all models of the objects that will returned to the user
via API endpoint responses.
"""

from pydantic import BaseModel
from typing import List


class AdjustedTemperature(BaseModel):
    location: str
    measure: int

    class Config:
        """Example data."""
        schema_extra = {
            'example': {
                'location': 'Drogenbos',
                'measure': 10
            }
        }
