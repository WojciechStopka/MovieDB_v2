from client import MoviesClient

if __name__ == "__main__":
	new_client = MoviesClient()
	new_client.get_popular_movies(15)
	new_client.get_rated_by_user_movies()
	new_client.get_average_user_rating()
	new_client.rated_movies_visualisation()
	new_client.popular_movies_visualisation()
