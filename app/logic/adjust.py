import logging
from sqlalchemy.orm import Session
from typing import List
from app.database import crud, models, schemas
from app.models.input_models import MeasuredTemperature


def adjust_temperature(
    measured_temperatures: List[MeasuredTemperature],
    db: Session
):
    """Return list of adjusted measures where each measure contains the min
    value of measured temperatures.

    1. Loop through the measured_temperature list.
    2. For each item, check location existance in DB.
    3. If location exist, update temperature keeping lowest value.
    4. If location does not exist, create location and link measure.
    """
    for measured_temperature in measured_temperatures:
        # Step 1: does location exist ?
        location = crud.get_location_by_name(
            db,
            name=measured_temperature.location
        )

        # Step 2: if it exists, compare current measurement and recorded min
        if location:
            logging.debug(f"Location [{measured_temperature.location}] exists")
            min_temp = location.measure.temperature
            if measured_temperature.measure < min_temp:
                crud.update_measure_by_id(
                    db,
                    measure=location.measure,
                    new_measure=measured_temperature.measure
                )

        # Step 3: if location does not exist, create location and set measure
        else:
            logging.debug(
                f"Location [{measured_temperature.location}] does "
                "not exist."
            )
            new_location = crud.create_location(
                db,
                location_name=measured_temperature.location
            )
            crud.create_location_measure(
                db,
                measure=measured_temperature.measure,
                location_id = new_location.id
            )

    measure_list = [
        dict(location=i.name, measure=i.measure.temperature)
        for i in crud.get_locations(db)
    ]


    return measure_list
