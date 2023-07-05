from client import MoviesClient
from visualization import popular_movies_visualisation, rated_movies_visualisation

if __name__ == "__main__":
	new_client = MoviesClient()
	rated_movies = new_client.get_rated_by_user_movies()
	popular_movies = new_client.get_popular_movies(15)
	average_score = new_client.get_average_user_rating()
	rated_movies_visualisation(rated_movies, average_score)
	popular_movies_visualisation(popular_movies)


