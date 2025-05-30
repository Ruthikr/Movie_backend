from flask import Flask
from flask_cors import CORS
from movie_search.routes import movie_blueprint  # Import the blueprint

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from the frontend

# Register the movie blueprint to handle the movie-related routes
app.register_blueprint(movie_blueprint)

if __name__ == '__main__':
    # Run the Flask app with debugging enabled
    app.run(debug=True)