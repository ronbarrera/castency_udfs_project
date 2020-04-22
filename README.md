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