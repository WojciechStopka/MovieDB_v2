from urllib.parse import urlencode

import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn as sns

import creds


class MoviesClient:
    """A class representing an API client for retrieving movie data from 'The Movie Database' API."""

    def __init__(self):
        """
        Initializes an instance of the ApiClient class.

        The constructor reads the authentication token and account ID from the corresponding file,
        initializes empty lists for popular and rated movies, and sets the average user rating to None.
        """
        self.auth_token = creds.auth_token
        self.account_id = creds.account_id
        self.popular_movies_list = []
        self.rated_movies_list = []
        self.average_user_rating = None

    def get_popular_movies(self, quantity=20):
        """
        Retrieves a list of popular movies from 'The Movie Database' API.

        Args:
            quantity (int): The number of popular movies to retrieve. Default is 20, because of maximum possible
            results to display on each page.

        Raises:
            Exception: If there is an error in retrieving the movie data. Displays a message describing an error.

        Returns:
            list: A list of dictionaries containing movie data, including title, average rating,
            and total number of votes.
        """
        movies_list = []
        endpoint = "https://api.themoviedb.org/3/discover/movie"
        headers = {"accept": "json", "Authorization": f"Bearer {self.auth_token}"}
        params = {"page": 0, "sort_by": "popularity.desc"}

        while len(movies_list) != quantity:
            if len(movies_list) % 20 == 0:
                params["page"] += 1
            params_encoded = urlencode(params)
            url = f"{endpoint}?{params_encoded}"
            response = requests.get(url, headers=headers)
            data = response.json()
            try:
                if not data["success"]:
                    raise Exception(f"{data['status_message']}")
            except KeyError:
                pass
            try:
                results = data["results"]
            except KeyError:
                raise KeyError("Sorry no results for popular movies")
            else:
                for movie in results:
                    if len(movies_list) < quantity:
                        movie_data = {
                            "Movie Title": movie["title"],
                            "Average rating": movie["vote_average"],
                            "Total number of votes": movie["vote_count"],
                        }
                        movies_list.append(movie_data)
        self.popular_movies_list = movies_list
        return movies_list

    def get_rated_by_user_movies(self):
        """
        Retrieves a list of movies rated by the user from 'The Movie Database' API.

        Raises:
            Exception: If there is an error in retrieving the movie data. Displays a message describing an error.

        Returns:
            list: A list of dictionaries containing movie data, including title, average rating,
            and user rating.
        """
        movies_list = []
        endpoint = (
            f"https://api.themoviedb.org/3/account/{self.account_id}/rated/movies"
        )
        headers = {"accept": "json", "Authorization": f"Bearer {self.auth_token}"}
        response = requests.get(endpoint, headers=headers)
        data = response.json()
        try:
            if not data["success"]:
                raise Exception(f"{data['status_message']}")
        except KeyError:
            pass
        try:
            results = data["results"]
        except KeyError:
            raise KeyError("Sorry no results for rated movies")
        else:
            for item in results:
                movie_data = {
                    "Movie Title": item["title"],
                    "Average rating": item["vote_average"],
                    "User rating": item["rating"],
                }
                movies_list.append(movie_data)
            self.rated_movies_list = movies_list
            return movies_list

    def get_average_user_rating(self):
        """
        Calculates the average user rating for the movies rated by the user.

        Returns:
            float: The average user rating.
        """

        if not self.rated_movies_list:
            return None
        total_ratings = len(self.rated_movies_list)
        total_user_rating = sum(
            [item["User rating"] for item in self.rated_movies_list]
        )
        average_rating = total_user_rating / total_ratings
        self.average_user_rating = average_rating
        return average_rating

    def popular_movies_visualisation(self):
        """
        Generates a bar plot visualizing the popular movies' data.

        The bar plot displays the movie title on the x-axis and the average rating on the y-axis.
        """
        df = pd.DataFrame(self.popular_movies_list)
        ax = sns.barplot(
            x="Movie Title",
            y="Average rating",
            data=df.sort_values("Average rating", ascending=False),
        )
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        plt.title("Popular movies")
        plt.show()

    def rated_movies_visualisation(self):
        """
        Generates a bar plot visualizing the movies rated by the user.

        The bar plot displays the movie title on the x-axis and the user rating on the y-axis.
        It also includes a red dashed line indicating the average user rating.
        """
        df = pd.DataFrame(self.rated_movies_list)
        ax = sns.barplot(x="Movie Title", y="User rating", data=df)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        if self.average_user_rating:
            plt.axhline(
                self.average_user_rating,
                ls="--",
                linewidth=3,
                color="red",
                label="Average user rating",
            )
            plt.legend()
        plt.title("Rated movies")
        plt.show()
