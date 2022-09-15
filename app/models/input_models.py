"""INPUT MODELS

This file contains all models of the objects that will enter the
application via API enpoints request bodies.
"""

from pydantic import BaseModel
from typing import List


class MeasuredTemperature(BaseModel):
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
