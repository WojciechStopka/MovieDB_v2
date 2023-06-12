# The Movie Database 
The Movie Database MoviesClient is a Python class that allows you to retrieve movie data from 'The Movie Database' API. This documentation provides an overview of the API client, its methods, and usage instructions.

## Goals
Within this project, I would like to explore the following:

- Getting familiar with **API**, **documentations** and **requests** library
- Practicing OOP
- Getting to know libraries such as **seaborn**, **matplotlib** and **pandas**
- Learning how to visualize stored data

## Table of Contents
- [1. Installation](https://github.com/WojciechStopka/project_moviedb#1-installation)
- [2. Authentication](https://github.com/WojciechStopka/project_moviedb#2-authentication)
- [3. Usage](https://github.com/WojciechStopka/project_moviedb#3-usage)
  - [3.1 Retrieving Popular Movies](https://github.com/WojciechStopka/project_moviedb#31-retrieving-popular-movies)
  - [3.2 Retrieving Movies Rated by User](https://github.com/WojciechStopka/project_moviedb#32-retrieving-movies-rated-by-user)
  - [3.3 Calculating Average User Rating](https://github.com/WojciechStopka/project_moviedb#33-calculating-average-user-rating)
  - [3.4 Visualizing Popular Movies](https://github.com/WojciechStopka/project_moviedb#34-visualizing-popular-movies)
  - [3.5 Visualizing Rated Movies](https://github.com/WojciechStopka/project_moviedb#35-visualizing-rated-movies)
- [4. Examples](https://github.com/WojciechStopka/project_moviedb#4-examples)
  - [4.1 Rated Movies](https://github.com/WojciechStopka/project_moviedb#41-rated-movies)
  - [4.2 10 Popular Movies](https://github.com/WojciechStopka/project_moviedb#42-10-popular-movies)
- [5. Ideas for improvements](https://github.com/WojciechStopka/project_moviedb#5-ideas-for-improvements)
- [6. Project limitations](https://github.com/WojciechStopka/project_moviedb#6-project-limitations)

## 1. Installation
To use the Movie Database MoviesClient, you need to have Python installed on your system. Additionally, you need to install the required dependencies: **pandas**, **requests**, **seaborn**, and **matplotlib**. You can install them using the following command:
```
pip install pandas requests seaborn matplotlib
```

## 2. Authentication
Before using the API client: 
- make sure you have an authentication token and account ID from 'The Movie Database' API. 
- Store the **authentication token** and **account ID** in a file named **creds.py**. These files should be located in the same directory as your Python script.

## 3. Usage
To use the Movie Database API Client, import the necessary libraries and create an instance of the MoviesClient class
```
from client import MoviesClient

new_client = MoviesClient()
```

### 3.1 Retrieving Popular Movies
To retrieve a list of popular movies, use the `get_popular_movies` method
```
new_client.get_popular_movies()
```
This method retrieves a list of popular movies from 'The Movie Database' API. The quantity parameter specifies the number of movies to retrieve (default is 20). The method returns a list of dictionaries containing movie data, including the **title**, **average rating**, and **total number of votes**.

### 3.2 Retrieving Movies Rated by User
To retrieve a list of movies rated by the user, use the `get_rated_by_user_movies` method.
```
new_client.get_rated_by_user_movies()
```
This method retrieves a list of movies rated by the user from 'The Movie Database' API. It returns a list of dictionaries containing movie data, including the **title**, **average rating** and **user rating**.

### 3.3 Calculating Average User Rating
To calculate the average user rating for the movies rated by the user, use the `get_average_user_rating` method.
```
new_client.get_average_user_rating()
```
This method calculates the average user rating for the movies rated by the user. It returns a float value representing the **average rating**. If there are no rated movies, it returns **None**.

### 3.4 Visualizing Popular Movies
To generate a bar plot visualizing the popular movies' data, use the `popular_movies_visualisation` method.
```
new_client.popular_movies_visualisation()
```
This method generates a bar plot displaying the **movie titles** on the x-axis and the **average ratings** on the y-axis. It requires the **seaborn**, **matplotlib.pyplot**, and **pandas** libraries to be installed.

### 3.5 Visualizing Rated Movies
To generate a bar plot visualizing the movies rated by the user, use the `rated_movies_visualisation` method.
```
new_client.rated_movies_visualisation()
```
This method generates a bar plot displaying the **movie titles** on the x-axis and the **user ratings** on the y-axis. It also includes a red dashed line indicating the **average user rating**.

## 4. Examples:
### 4.1 Rated Movies
![example 1](https://github.com/WojciechStopka/restaurant_finder_v2/assets/44327221/2e10b328-7732-409e-a931-11bfed1ae30c)

### 4.2 10 Popular Movies
![example 2](https://github.com/WojciechStopka/restaurant_finder_v2/assets/44327221/466fa00d-634d-4993-81f6-83a1f63d81f0)

## 5. Ideas for improvements
- Displaying information about specific movie such as **description**, **image**, **year of production**, **genre**.
- Making user-friendly GUI for better user experience.
- Helping user to find similar movies by passed title.
- Making feature to randomize movie above given rating.

## 6. Project limitations
- Displaying just unfiltered popular movies.
- Displaying just unfiltered rated by user movies.
