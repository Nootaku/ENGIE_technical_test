# Yet another technical test

[![Author](https://img.shields.io/badge/Developer-Maxime_Wattez-informational?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/Nootaku)<br/>![Vue](https://img.shields.io/badge/Last_Update-Sept_15,_2022-lightgrey?style=for-the-badge)<br/>![Vue](https://img.shields.io/badge/Version-0.0.1-yellow?style=for-the-badge&logo=Git)

[![Vue](https://img.shields.io/badge/Framework-FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=#009688)](https://fastapi.tiangolo.com/)

## Objective of the test

Create a *REST API* with one endpoint `/adjust` expecting a **JSON body** containing a list of measured temperatures by location.

Keep track of the *minimal temperatures* in a database.

Make sure the locations are stored in a separate table and a foreign key is used. Please use **SqlAlchemy** as an ORM.

Return a **JSON response** with the new of minimal temperatures by location.

The project does not need to contain the whole setup to make it deployable. However, in addition to the code of the application, it should contain a **test suite** ensuring that those specifications are matched.  

Below is a sample API request with the expected response (HTTP 200).<br/>In the example `Drogenbos` should be updated  to `9`, because the measured temperature is lower than previous minimum. `Tihange` should be added and set to `11` because it was not yet present in the minima. Other minimum values (`Doel` and `Stade`) are unchanged.

*Example input:*

```json
[
    {
        "location": "Doel",
        "measure": 11
    },
    {
		"location": "Drogenbos",
		"measure": 9
	},
	{
		"location": "Tihange",
		"measure": 11
	}
]
```



*Example output:*

```json
[
    {
        "location": "Doel",
        "measure": 10
	},
	{
		"location": "Drogenbos",
		"measure": 9
	},
	{
		"location": "Stade",
		"measure": 10
	},
	{
		"location": "Tihange",
		"measure": 11
	}
]
```



## Installation and usage

### Installation

This installation has been written under the assumption that you have **Python 3.10** and **PIP** installed on your machine or in your virtual environment.

```bash
# Clone repo
git clone https://foo/bar

# Install dependencies
cd engie_2
pip install -r requirements.txt
```



### Usage

To run the API you have 2 options:

```bash
# Option 1: Uvicorn
uvicorn app.main:app

# Option 2: Python
python app/main.py
```



### Testing

The setup of the testing environment is following the good practices recommended by PyTest: [see documentation](https://docs.pytest.org/en/7.1.x/explanation/goodpractices.html).

```bash
pip install -e .
pytest
```



## Proposed solution

### Structure

```bash
.
├── database
│   ├── crud.py
│   ├── database.db
│   ├── db_init.py
│   └── schemas.py
├── logic
│   ├── adjust.py
├── main.py
└── models
    ├── db_models.py
    ├── input_models.py
    └── output_models.py
```

The API instance is created in `main.py`.  The `database` directory contains all the logic relative to the connection with the database. The `logic` directory contains the business logic. Finally the `models` directory contains all the models that are used as input for both the endpoints and the database.

### Database

We have decided to use an SQLite database since it is a unique file that is easy to share. Moreover, Python has native support for this type of database.

#### Connection

The main connection to the database is done in `db_init` 









https://atom.io/packages/linter

https://fastapi.tiangolo.com/tutorial/first-steps/

https://pydantic-docs.helpmanual.io/usage/models/
