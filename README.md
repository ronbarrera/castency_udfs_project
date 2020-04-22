# Castency - UDFS Nanodegree Capstone Project API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

To run the server, execute:

```bash
flask run
```

The `--reload` flag will detect file changes and restart the server automatically.

## API Reference

### Getting Started
- The backend app is hosted at default: `https://casting-agency-udfs.herokuapp.com/`

### Endpoints

#### GET `/actors`
- General:
    - Returns a list of actors objects, categories dictionary, total number of actors and success value.

- Sample: ` curl https://casting-agency-udfs.herokuapp.com/actors -H "Authorization: Bearer <Token>"`
- Response:
```{
        {
            "actors": [
                {
                    "age": 47,
                    "gender": "Female",
                    "id": 2,
                    "name": "Rhea Seehorn"
                }
            ],
            "success": true,
            "total_actors": 1
        }
 ```


#### GET `/movies`
- General:
    - Returns a list of movies objects, categories dictionary, total number of movies and success value.

- Sample: ` curl https://casting-agency-udfs.herokuapp.com/movies -H "Authorization: Bearer <Token>"`
- Response:
```{
        {
            "movies": [
                {
                    "id": 1,
                    "release_date": "04/22/20",
                    "title": "Inception"
                }
            ],
            "success": true,
            "total_movies": 1
        }
 ```

#### POST `/actors`
- General:
    - Creates a new actor using the name, age, and gender. Returns the id of the created actor, success value, and the new actor object. 

- Sample: ` curl -X POST https://casting-agency-udfs.herokuapp.com/actors -H "Authorization: Bearer <Token>" -H "Content-Type: application/json" -d '{"name": "Rhea Seehorn", "age": 47, "gender": "Female"}'`
- Response:
```{
        {
            "actors": {
                "age": 47,
                "gender": "Female",
                "id": 15,
                "name": "Rhea Seehorn"
            },
            "created": 15,
            "success": true
        }
 ```

#### POST `/movies`
- General:
    - Creates a new movie using the title, and release_date. Returns the id of the created movie, success value, and the new movie object. 

- Sample: ` curl -X POST https://casting-agency-udfs.herokuapp.com/movies -H "Authorization: Bearer <Token>" -H "Content-Type: application/json" -d '{"title": "Inception", "release_date": "4/22/20"}'`
- Response:
```{
        {
            "created": 1,
            "movies": {
                "id": 1,
                "release_date": "04/22/20",
                "title": "Inception"
            },
            "success": true
        }
 ```

#### DELETE `/actors/<int:actor_id>`
- General:
    - Deletes the actor of the given id if it exists. Returns the id of the deleted actor and success value.  

- Sample: ` curl -X DELETE https://casting-agency-udfs.herokuapp.com/actors/15 -H "Authorization: Bearer <Token>"`
- Response:
```{
        {
            "deleted": 15,
            "success": true
        }
 ```

#### DELETE `/movies/<int:movie_id>`
- General:
    - Deletes the movie of the given id if it exists. Returns the id of the deleted movie and success value.  

- Sample: ` curl -X DELETE https://casting-agency-udfs.herokuapp.com/movie/1 -H "Authorization: Bearer <Token>"`
- Response:
```{
        {
            "deleted": 1,
            "success": true
        }
 ```

#### PATCH `/actors/<int:actor_id>`
- General:
    - Partially updates the content of the given id actor. Returns updated actor and success value. 

- Sample: ` curl -X PATCH https://casting-agency-udfs.herokuapp.com/actors/21 -H "Authorization: Bearer <Token>" -H "Content-Type: application/json" -d '{"name": "Ronald Barrera", "gender": "Male"}'`
- Response:
```{
       {
            "success": true,
            "updated": {
                "age": 47,
                "gender": "Male",
                "id": 21,
                "name": "Ronald Barrera"
            }
        }
 ```

#### PATCH `/movies/<int:movie_id>`
- General:
    - Partially updates the content of the given id movie. Returns updated movie and success value. 

- Sample: ` curl -X PATCH https://casting-agency-udfs.herokuapp.com/movies/4 -H "Authorization: Bearer <Token>" -H "Content-Type: application/json" -d '{""title": "Friday"}'`
- Response:
```{
       {
            "success": true,
            "updated": {
                "id": 4,
                "release_date": "04/22/20",
                "title": "Friday"
            }
        }
 ```

## Permissions
- `get:actors` **Get all actors saved on the db**
- `get:movies` **Get all movies saved on the db**
- `post:actors` **Can add a new actor to the db**
- `post:movies` **Can add a new movie to the db**
- `delete:actors` **Can delete an actor from the db**
- `delete:movies` **Can delete a movie from the db**
- `patch:actors` **Can partially update an actor from the db**
- `patch:movies` **Can partially update a movie from the db**

## Roles
- **Casting Assistant:** `get:actors`, `get:movies`
- **Casting Director:** `get:actors`, `get:movies`, `post:actors`, `delete:actors`, `patch:actors`, `patch:movies`
- **Executive Producer:** `get:actors`, `get:movies`, `post:actors`, `delete:actors`, `patch:actors`, `patch:movies`, `post:movies`, `delete:movies`

## Tokens
The following JWT were used to test all endpoints.  

**Casting Assistant JWT:**
``eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVWakhNTnd0WW5VXy0yRERPX29DZyJ9.eyJpc3MiOiJodHRwczovL3JvbmFsZGJhcnJlcmEuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlOTVmOTExMDJkYTdlMGM2MjQ5YzI0OSIsImF1ZCI6ImNhc3RlbmN5IiwiaWF0IjoxNTg3NTM5MTA2LCJleHAiOjE1ODc1NDYzMDYsImF6cCI6ImwzeGZJMjV3ak9ZZm5CVVprT1h3RW55eVFUeWRLRzMwIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.WLPjTUzwPLi7IrSGLzj42en3VxjFogxDgEdnr_tKd9agsSLDt7NCyWxknQJC8YQXtmTlyEBrfdt74W0o0QnnsXhiqqFRJ-tOL8a_HwusjPLgeX_J1sCl5guHb0G3Ohg7-PZBDviV2tngtkFzriFPMyVxDK8PUVMo2eveC1IsJWB3MU4alrjTyo8RkPTp_RToYUoM5WVwkCii_00RQvgPc5_w1MChxxwXMGgQgvh_uguWcLBFlFx-VZrALzE_5gC1CofChCDa95WwgK65lunVRdZZrAdn9wCLIufJQ39Xh9Dz7uuws2mvr93RJrY6fsTQJbWSowG1L7mxVN-rBK6wWA``

**Casting Director JWT:**
``eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVWakhNTnd0WW5VXy0yRERPX29DZyJ9.eyJpc3MiOiJodHRwczovL3JvbmFsZGJhcnJlcmEuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTExOTA4NDM5ODA1MTkwMzA5MTY5IiwiYXVkIjpbImNhc3RlbmN5IiwiaHR0cHM6Ly9yb25hbGRiYXJyZXJhLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1ODc1NDE3MTksImV4cCI6MTU4NzU0ODkxOSwiYXpwIjoibDN4ZkkyNXdqT1lmbkJVWmtPWHdFbnl5UVR5ZEtHMzAiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.TqlRl30bjw3KCSOR5Lx--FFRqQ6Cjc9_0G_knwIy34ioAaAT6aO5ICqb9becxwFJ0gSxapWGuCtY_AWoa-BkzQYSRYPAiS1horvIPC7Z8fz8V9RjSt28HU3F_TjC4rANqazuLvYI57sMexK3lZVwkZhefYaDXX8NL99qrewTJFaYDXz7PpSU85NCJTMHdt0RclWjFmkVb5xpTnWuEavwctdCqOHxdu8L2YfxhO5G5yeUiIw5lVoIxIuOpdgaKuP8kDIJoQ2PuHum_TBELJoNoF89W0pZM4UOtvWyr-QIeqUmj7158mPca7S-BEAfnrGiXY7T9RZSIU6ilZjj9TYTkg``

**Executive Producer JWT:**
``eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVWakhNTnd0WW5VXy0yRERPX29DZyJ9.eyJpc3MiOiJodHRwczovL3JvbmFsZGJhcnJlcmEuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTEwNjE1OTI3NjM5Njg1MDA1MTgyIiwiYXVkIjpbImNhc3RlbmN5IiwiaHR0cHM6Ly9yb25hbGRiYXJyZXJhLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1ODc1Mzg1MjEsImV4cCI6MTU4NzU0NTcyMSwiYXpwIjoibDN4ZkkyNXdqT1lmbkJVWmtPWHdFbnl5UVR5ZEtHMzAiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.Y8haa-MqaIyTydQ2yYS-Ds_MyXWZFb21ysSh9eqQm2LAp7oCOW80fPAhR0xBuS-rbZnobKKnIQLiVB-i-Fc_lVIiSsDd1G2E7XxnToG3OulpWZYoh3CyjTrKiNfoJQGoCxLD-yrP6rz_Sn7FisBxMqhbzmIYNPSEsAiwSM_axtnIziGzVMvTx-UfyQY_4kVD8aUvt5WDIO8F5qrhyVWR3p-Dqi-d9vNlZlG0cFdVwKsbVnJtWGJbinp_6KH4PJ6nclsIeQvxjD8oFlTCo-tPse6nJ94uxFvibdGiEUsj_1FjLGyi_i8nXBTftb8uc0UaKw0ZfYP8_99oCbhGdzmMcA``