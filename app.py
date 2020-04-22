import os
import datetime
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actor, Movie

from auth import AuthError, requires_auth

def create_app(test_config=None):
	# create and configure the app
	app = Flask(__name__)
	setup_db(app)
	CORS(app)

	@app.route('/')
	def index():
		return 'Not Implemented.'

	#  Actor
	#  ----------------------------------------------------------------
	@app.route('/actors')
	@requires_auth('get:actors')
	def get_actors(jwt):
		actors = Actor.query.all()
		formatted_actors = [actor.format() for actor in actors]
		return jsonify({
			'actors': formatted_actors,
			'total_actors': len(actors),
			'success': True
		})
	
	@app.route('/actors', methods=['POST'])
	@requires_auth('post:actors')
	def create_actor(jwt):
		try: 
			body = request.get_json()
			name = body.get('name')
			age = body.get('age')
			gender = body.get('gender')
			actor = Actor(name=name, age=age, gender=gender) 
			actor.insert()
			return jsonify({
				'success': True, 
				'actors': actor.format()
			})
		except BaseException:
			abort(422)
	
	@app.route('/actors/<int:actor_id>', methods=['DELETE'])
	@requires_auth('delete:actors')
	def delete_actor(jwt, actor_id):
		try:
			actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
			if actor is None:
				abort(404)
			actor.delete()
			return jsonify({
				'success': True, 
				'deleted': actor_id
			})
		except BaseException:
			abort(422)

	@app.route('/actors/<int:actor_id>', methods=['PATCH'])
	@requires_auth('patch:actors')
	def update_actor(jwt, actor_id):
		try: 
			actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
			if actor is None: 
				abort(404)
			body = request.get_json()
			actor.name = body.get('name', actor.name)
			actor.age = body.get('age', actor.age)
			actor.gender = body.get('gender', actor.gender)
			actor.update()
			return jsonify({
				'success': True, 
				'updated': actor.format()
			})
		except BaseException: 
			abort(422)

	#  Movie
	#  ----------------------------------------------------------------
	@app.route('/movies')
	@requires_auth('get:movies')
	def get_movies(jwt):
		movies = Movie.query.all()
		formatted_movies = [movie.format() for movie in movies]
		return jsonify({
			'movies': formatted_movies, 
			'total_movies': len(movies), 
			'success': True
		})

	@app.route('/movies', methods=['POST'])
	@requires_auth('post:movies')
	def create_movie(jwt):
		try: 
			body = request.get_json()
			title = body.get('title')
			release_date = body.get('release_date')
			movie = Movie(title=title, release_date=release_date)
			movie.insert()
			return jsonify({
				'success': True
			})
		except BaseException: 
			abort(422)

	@app.route('/movies/<int:movie_id>', methods=['DELETE'])
	@requires_auth('delete:movies')
	def delete_movie(jwt, movie_id):
		try:
			movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
			if movie is None: 
				abort(404)
			movie.delete()
			return jsonify({
				'success': True, 
				'deleted': movie_id
			})
		except BaseException:
			abort(422)

	@app.route('/movies/<int:movie_id>', methods=['PATCH'])
	@requires_auth('patch:movies')
	def update_movie(jwt, movie_id):
		try:
			movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
			if movie is None: 
				abort(404)
			body = request.get_json()
			movie.title = body.get('title', movie.title)
			movie.release_date = body.get('release_date', movie.release_date)
			movie.update()
			return jsonify({
				'success': True, 
				'updated': movie.format()
			})
		except BaseException:
			abort(422)

	@app.errorhandler(400)
	def bad_request(error):
		return jsonify({
			"success": False, 
			"error": 400, 
			"message": "bad request"
		}), 400
	
	@app.errorhandler(404)
	def not_found(error):
		return jsonify({
			"success": False, 
			"error": 404, 
			"message": "resource not found"
		}), 404
	
	@app.errorhandler(422)
	def unprocessable(error):
		return jsonify({
			"success": False, 
			"error": 422,
			"message": "unprocessable"
		}), 422

	@app.errorhandler(AuthError)
	def handle_authentication_error(ex):
		ex.error.update({"success": False})
		response = jsonify(ex.error)
		response.status_code = ex.status_code
		return response

	return app

app = create_app()

if __name__ == '__main__':
	app.run()
  	# APP.run(host='0.0.0.0', port=8080, debug=True)