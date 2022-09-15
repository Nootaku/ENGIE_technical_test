from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from typing import List
from app.database import crud, models, schemas
from app.database.database import SessionLocal, engine
from app.models.input_models import MeasuredTemperature
from app.models.output_models import AdjustedTemperature
from app.logic.adjust import adjust_temperature

app = FastAPI()

# DB Dependency
def get_db():
    """Function to be added as dependency to an API endpoint.
    When the API endpoint is called, this function will be called yielding the
    DB.
    When the API call is over, this function will close the connection to the
    DB.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get(
    "/",
    response_class=HTMLResponse
)
async def root():
    """HTML message indicating to the user that another endpoint is available.
    """
    return """
    <html>
        <head>
            <title="Engie API">
        </head>
        <body>
            <div>
                <h3>Welcome to the Engie API</h3>
            </div>
            <div>
                <p>This API is composed of 3 endpoints:</p>
                <ul>
                    <li>Root page: this page tells you about this API.</li>
                    <li><a href="/docs">Documentation page</a>: Swagger documentation of the API</li>
                    <li>The <a href="/adjust">adjust endpoint</a>: requested endpoint.</li>
            </div>
        </body>
    </html>
    """


@app.post(
    "/adjust",
    # response_model=List[AdjustedTemperature]
)
async def adjust(
    measured_temperatures: List[MeasuredTemperature],
    db: Session = Depends(get_db)
):
    """some docstring
    """
    adjusted_temperatures = adjust_temperature(
        measured_temperatures=measured_temperatures,
        db=db
    )
    return adjusted_temperatures


if __name__ == '__main__':
    import uvicorn
    # Default host = '127.0.0.1'
    # App name can also be `api`, but a string is required for `reload=True`
    uvicorn.run('app.main:app', port=5000, reload=True)
