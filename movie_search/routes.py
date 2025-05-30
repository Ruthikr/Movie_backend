from flask import Blueprint, jsonify, request
from movie_search.movie_service import search_movie_details

# Create a blueprint for movie-related routes
movie_blueprint = Blueprint('movies', __name__)

@movie_blueprint.route('/search', methods=['GET'])
def search_movie():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'No query parameter provided'}), 400

    # Call the search_movie_details function from the service
    results = search_movie_details(query)
    return jsonify(results)

# You can add more routes as needed