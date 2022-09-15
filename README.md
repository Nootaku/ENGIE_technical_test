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



## Solution proposée

### Base de Donnée

Tout d'abord, nous utiliserons SQLite comme base de donnée car il s'agit d'un fichier unique qui est facile à partager. De plus, Python supporte ce type de fichier par défaut.









https://atom.io/packages/linter

https://fastapi.tiangolo.com/tutorial/first-steps/

https://pydantic-docs.helpmanual.io/usage/models/
