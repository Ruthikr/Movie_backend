import requests

API_KEY = '2O3w278YolWV4hnFPeNZAcu78v01mBRuKIL2YVfm'
SEARCH_URL = 'https://api.watchmode.com/v1/search/'
MOVIE_DETAILS_URL = 'https://api.watchmode.com/v1/title/{title_id}/details/'
AUTOSEARCH_URL="https://api.watchmode.com/v1/autocomplete-search/"
#SOURCES_URL='https://api.watchmode.com/v1/title/{title_id}/sources/'

def search_movie_details(query, limit=5):  # You can set the limit here (3 or 5)
    # Search for movies
    response = requests.get(AUTOSEARCH_URL, params={'apiKey': API_KEY, 'search_value': query,
     'search_type':2
       })
    data = response.json()

    if not data.get('results'):
        return {'error': 'No movies found'}

    # Limit to top `limit` search results
    if len(data['results'])>limit:
        limited_results = data['results'][:limit]
    else:
        limited_results=data["results"]
    movies = []
    for movie in limited_results:
        movie_id = movie['id']
        
        # Get movie details
        movie_details_response = requests.get(MOVIE_DETAILS_URL.format(title_id=movie_id), params={'apiKey': API_KEY,
          'append_to_response':'sources'
        })
        
        '''
        movie_sources_response=requests.get(SOURCES_URL.format(title_id=movie_id),params={'apiKey':API_KEY})
        '''
        movie_details = movie_details_response.json()
        '''
        movie_sources=movie_sources_response.json()
         sources=[]
        for s in movie_sources:
            sources.append({
          "name":s.get("name","N/A"),
          "price":s.get("price","N/A"),
          "format":s.get("format","N/A"),
          "web_url":s.get("web_url")
        })
        '''
      
        movies.append({
          "available_on":movie_details.get("sources","N/A"),
          "id":movie_details.get("id","N/A"),
          "original_title":movie_details.get("original_title","N/A"),
          "title":movie_details.get("title","N/A"),
          "backdrop_img":movie_details.get("backdrop","N/A"),
          "poster_img":movie_details.get("poster","N/A"),
          "critic_score":movie_details.get("critic_score","N/A"),
          "genre_names":movie_details.get("genre_names","N/A"),
          "original_language":movie_details.get("original_language","N/A"),
          "plot_overview":movie_details.get("plot_overview","N/A"),
          "release_date":movie_details.get("release_date","N/A"),
          "relevance_percentile":movie_details.get("relevance_percentile","N/A"),
          "runtime_minutes":movie_details.get("runtime_minutes","N/A"),
          "tmdb_type":movie_details.get("tmdb_type","N/A"),
          "trailer":movie_details.get("trailer","N/A"),
          "trailer_thumbnai":movie_details.get("trailer_thumbnail","N/A"),
          "type":movie_details.get("type","N/A"),
          "user_rating":movie_details.get("user_rating","N/A"),
          "us-rating":movie_details.get("us-rating","N/A"),
          "year":movie_details.get("year","N/A")
        })
        
        
        
    return movies




'''
def search_movie_details(query):
    try:
        # Search for movies by query
        response = requests.get(SEARCH_URL, params={'apiKey': API_KEY, 'search_field': 'name', 'search_value': query})
        data = response.json()
        
        if not data.get("title_results"):
            return {'error': 'No movies found'}
        data=data["title_results"][:1]
        movies = []
        for movie in data:
            movies.append(movie["imdb_id"])
        # Check if the response contains title_results
        results=[]
        for i in movies:
              # Get movie details
            movie_details_response = requests.get(MOVIE_DETAILS_URL.format(imdb_id=i), params={'apiKey': API_KEY})
            results.append(movie_details_response)
        
            
        
        final={"results":results}
        # Return the top 3 results
        return final

    except requests.RequestException as e:
        return {'error': 'Failed to fetch movie details', 'details': str(e)}
  '''
'''
def after():
  movie_sources_response=requests.get(SOURCES_URL.format(imdb_id=i),params={'apiKey':API_KEY})
  '''
