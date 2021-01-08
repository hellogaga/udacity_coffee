# Coffee Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Tasks

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `get:drinks-detail`
    - `post:drinks`
    - `patch:drinks`
    - `delete:drinks`
6. Create new roles for:
    - Barista
        - can `get:drinks-detail`
    - Manager
        - can perform all actions
7. Test your endpoints with [Postman](https://getpostman.com). 
    - Register 2 users - assign the Barista role to one and Manager role to the other.
    - Sign into each account and make note of the JWT.
    - Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
    - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
    - Run the collection and correct any errors.
    - Export the collection overwriting the one we've included so that we have your proper JWTs during review!

### Implement The Server

There are `@TODO` comments throughout the `./backend/src`. We recommend tackling the files in order and from top to bottom:

1. `./src/auth/auth.py`
2. `./src/api.py`


### Auth0 Manager
```
https://hellogaga.eu.auth0.com/authorize?audience=coffeeshop&response_type=token&client_id=Vnzko1rzSDYHPNbXA9Wnef77ihHfLFSr&redirect_uri=http://localhost:5000/
```

Return<br>
```
http://localhost:5000/#access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlozRjRBeDlsUWRuYms0ZV9fdDBrMSJ9.eyJpc3MiOiJodHRwczovL2hlbGxvZ2FnYS5ldS5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDYzNDc1Nzg1MjAzNDQyOTMzNDMiLCJhdWQiOlsiY29mZmVlc2hvcCIsImh0dHBzOi8vaGVsbG9nYWdhLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTAxNDA3NjEsImV4cCI6MTYxMDE0Nzk2MSwiYXpwIjoiVm56a28xcnpTRFlIUE5iWEE5V25lZjc3aWhIZkxGU3IiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.IgYhthRvh9V_VhgJ5Rz4dhz-SzItlCf5kd7tlbQIhf1btP1zeh6O2m37bBefF2J0sCB_WfPwPaaf8AbN3NfJ3OAhJ1AbpsmNGcUTE6eXxS5bi_j0WsxWz29POgiyDSJJmiYkcdGMZ61HCChSjOXRMiHFL6r7q_tkcQTkktHmQ22CWfxULOAkQDRlTtvnS5ITWdZvBXf23Sx5MLMYmkUc9I6yD1VLgk7zbKL2bgCEAf2qQDkj5jf2FjPYPmNq4LYiH1ZLlXs3_ivnta0xnUtM9fvqOJvqyzmtPuTNrler25TsHTRLa42p8S71c01g1IDwNyUGt3k_flk3S8kJEMdZxw&scope=openid%20profile%20email&expires_in=7200&token_type=Bearer&state=g6Fo2SA0Ujhha2ZxQmxveFFXREk5RDhTXzdUTUlpaFM5b1lWN6N0aWTZIEloMEYtTU9yMnRzTnhRbG11YW9URVlWUWNGY2tFSjVJo2NpZNkgVm56a28xcnpTRFlIUE5iWEE5V25lZjc3aWhIZkxGU3I
```

```jwt
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlozRjRBeDlsUWRuYms0ZV9fdDBrMSJ9.eyJpc3MiOiJodHRwczovL2hlbGxvZ2FnYS5ldS5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDYzNDc1Nzg1MjAzNDQyOTMzNDMiLCJhdWQiOlsiY29mZmVlc2hvcCIsImh0dHBzOi8vaGVsbG9nYWdhLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTAxNDA3NjEsImV4cCI6MTYxMDE0Nzk2MSwiYXpwIjoiVm56a28xcnpTRFlIUE5iWEE5V25lZjc3aWhIZkxGU3IiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.IgYhthRvh9V_VhgJ5Rz4dhz-SzItlCf5kd7tlbQIhf1btP1zeh6O2m37bBefF2J0sCB_WfPwPaaf8AbN3NfJ3OAhJ1AbpsmNGcUTE6eXxS5bi_j0WsxWz29POgiyDSJJmiYkcdGMZ61HCChSjOXRMiHFL6r7q_tkcQTkktHmQ22CWfxULOAkQDRlTtvnS5ITWdZvBXf23Sx5MLMYmkUc9I6yD1VLgk7zbKL2bgCEAf2qQDkj5jf2FjPYPmNq4LYiH1ZLlXs3_ivnta0xnUtM9fvqOJvqyzmtPuTNrler25TsHTRLa42p8S71c01g1IDwNyUGt3k_flk3S8kJEMdZxw
```

### Auth0 Brista

```
http://localhost:5000/#access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlozRjRBeDlsUWRuYms0ZV9fdDBrMSJ9.eyJpc3MiOiJodHRwczovL2hlbGxvZ2FnYS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZmODkwOWM4ZWZlMDIwMDY4YzBjMWQ1IiwiYXVkIjoiY29mZmVlc2hvcCIsImlhdCI6MTYxMDEzOTM3OSwiZXhwIjoxNjEwMTQ2NTc5LCJhenAiOiJWbnprbzFyelNEWUhQTmJYQTlXbmVmNzdpaEhmTEZTciIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRyaW5rcy1kZXRhaWwiXX0.DPeGhoXzN5w3nTYf-tE-95iTaaQhGf9ka6y1Oi2dx83nAMn5U-fMZUCcRIBC7WJG1JjzoYLdtLOuib8lIhPE_dp4oc-b5o0uQmC0LSu15iI1h6lzNmGUAzAuFMIS9oEv5bdvuLfR-KrvT99Xk4vZflLGLir4UP3-0waBbzzzbpWJNLUBCQkYRoDrJHZYQ7O5Dtlafhs19dxHilJqnTADu2rmr7HtAeT5rhkyM21B0RWi8K-dR9NpS3ovkh5uf2osjq1ydqxUcuvRJ3RHDNPzDLIPdqAdgPwE93cV_9drcgzKMUtdluU5gxriJumODwcE47XLrCPIzIgLsdsUkDsK6w&expires_in=7200&token_type=Bearer
```
```jwt
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlozRjRBeDlsUWRuYms0ZV9fdDBrMSJ9.eyJpc3MiOiJodHRwczovL2hlbGxvZ2FnYS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZmODkwOWM4ZWZlMDIwMDY4YzBjMWQ1IiwiYXVkIjoiY29mZmVlc2hvcCIsImlhdCI6MTYxMDEzOTM3OSwiZXhwIjoxNjEwMTQ2NTc5LCJhenAiOiJWbnprbzFyelNEWUhQTmJYQTlXbmVmNzdpaEhmTEZTciIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRyaW5rcy1kZXRhaWwiXX0.DPeGhoXzN5w3nTYf-tE-95iTaaQhGf9ka6y1Oi2dx83nAMn5U-fMZUCcRIBC7WJG1JjzoYLdtLOuib8lIhPE_dp4oc-b5o0uQmC0LSu15iI1h6lzNmGUAzAuFMIS9oEv5bdvuLfR-KrvT99Xk4vZflLGLir4UP3-0waBbzzzbpWJNLUBCQkYRoDrJHZYQ7O5Dtlafhs19dxHilJqnTADu2rmr7HtAeT5rhkyM21B0RWi8K-dR9NpS3ovkh5uf2osjq1ydqxUcuvRJ3RHDNPzDLIPdqAdgPwE93cV_9drcgzKMUtdluU5gxriJumODwcE47XLrCPIzIgLsdsUkDsK6w
```

https://hellogaga.eu.auth0.com/.well-known/jwks.json