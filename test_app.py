import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie

class CastencyTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "castency_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        setup_db(self.app, self.database_path)

        self.new_actor = {
            'name': 'Rhea Seehorn',
            'age': 47,
            'gender': 'Female'
        }

        self.new_movie = {
            'title': 'El Camino: A Breaking Bad Movie', 
            'release_date': '10/07/2019'
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """ Actor Endpoint """

    def test_get_actors(self):
        res = self.client().get('/actors')
        data = res.get_json()
        actors = Actor.query.all()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actors'], [actor.format() for actor in actors])

    def test_create_new_actor(self):
        res = self.client().post('/actors', json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['actors'])

    def test_delete_actor(self):
        res = self.client().post('/actors', json=self.new_actor)
        created_data = json.loads(res.data)
        created_id = created_data['created']

        res = self.client().delete('/actors/' + str(created_id))
        data = json.loads(res.data)

        deleted_actor = Actor.query.filter(Actor.id == created_id).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], created_id)
        self.assertEqual(deleted_actor, None)

    def test_422_if_actor_does_not_exist(self):
        res = self.client().delete('/actors/10000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_update_actor(self):
        res = self.client().post('/actors', json=self.new_actor)
        created_data = json.loads(res.data)
        created_id = created_data['created']
        updated_actor = { 'age': 29 }
        
        res = self.client().patch('/actors/' + str(created_id), json=updated_actor)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['updated']['age'], 29)

    """ Movie Endpoint """

    def test_get_amovies(self):
        res = self.client().get('/movies')
        data = res.get_json()
        movies = Movie.query.all()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movies'], [movie.format() for movie in movies])

    def test_create_new_movie(self):
        res = self.client().post('/movies', json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['movies'])

    def test_delete_movie(self):
        res = self.client().post('/movies', json=self.new_movie)
        created_data = json.loads(res.data)
        created_id = created_data['created']

        res = self.client().delete('/movies/' + str(created_id))
        data = json.loads(res.data)

        deleted_movie = Movie.query.filter(Movie.id == created_id).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], created_id)
        self.assertEqual(deleted_movie, None)

    def test_422_if_movie_does_not_exist(self):
        res = self.client().delete('/movies/10000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_update_Movie(self):
        res = self.client().post('/movies', json=self.new_movie)
        created_data = json.loads(res.data)
        created_id = created_data['created']
        updated_movie = { 'release_date': '04/21/20' }
        
        res = self.client().patch('/movies/' + str(created_id), json=updated_movie)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['updated']['release_date'], '04/21/20')
        

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()