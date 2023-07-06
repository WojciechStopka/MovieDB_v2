import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def popular_movies_visualisation(popular_movies):
    """
    Generates a bar plot visualizing the popular movies' data.

    The bar plot displays the movie title on the x-axis and the average rating on the y-axis.
    """
    df = pd.DataFrame(popular_movies)
    ax = sns.barplot(
        x="Movie Title",
        y="Average rating",
        data=df.sort_values("Average rating", ascending=False),
    )
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    plt.title("Popular movies")
    plt.show()


def rated_movies_visualisation(rated_movies, average_score):
    """
    Generates a bar plot visualizing the movies rated by the user.

    The bar plot displays the movie title on the x-axis and the user rating on the y-axis.
    It also includes a red dashed line indicating the average user rating.
    """
    df = pd.DataFrame(rated_movies)
    ax = sns.barplot(x="Movie Title", y="User rating", data=df)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    if average_score:
        plt.axhline(
            average_score,
            ls="--",
            linewidth=3,
            color="red",
            label="Average user rating",
        )
        plt.legend()
    plt.title("Rated movies")
    plt.show()
