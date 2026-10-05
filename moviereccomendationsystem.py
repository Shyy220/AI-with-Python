import pandas as pd
import time
from colorama import init, Fore

init(autoreset=True)

try:
    df = pd.read_csv("imdb_top_1000 copy.csv")
except FileNotFoundError:
    print(Fore.RED + "Error: idmb_top_1000.csv file not found!")
    exit()


genres = []

for items in df["Genre"]:
    genre_list = items.split(", ")

    for genre in genre_list:
        if genre not in genres:
            genres.append(genre)

genres.sort()

def processing_animation():

    print(Fore.YELLOW + "\nFinding movies", end="")

    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()

def display_genres():

    print(Fore.CYAN + "\n===========AVAILABLE GENRES=========\n")

    for i in range(len(genres)):
        print(f"{i+1}. {genres[i]}")

def get_genre():

    while True:

        choice = input(
            Fore.YELLOW +
            "\nEnter Genre Name:" 
        ).title()

        if choice in genres:
            return choice

        print(Fore.RED + "Invalid Genre! Please Try Again.")

def get_rating():

    while True:

        rating = input(
            Fore.YELLOW +
            "Enter Minimum IDMB Rsting(or type skip): "
        )

        if rating.lower() == "skip":
            return None

        try:
            return float(rating)

        except ValueError:
            print(Fore.RED + "Please enter a valid number.")

def reccomend_movies(genre, min_rating):

    movies=[]

    for index, row in df.iterrows():

        movie_genre = row["Genre"]
        movie_rating = row["IDMB_Rating"]

        if genre in movie_genre:

            if min_rating is None or movie_rating >= min_rating:

                movies.append(
                    (
                        row["Series_title"],
                        movie_rating
                    )
                )
            if len(movies) == 5:
                break

        return movies


def display_movies(movie_list, name):

    print(
        Fore.GREEN +
        f"\n Reccomended Movies for {name}\n"
    )

    if len(movie_list) == 0:
        print(Fore.RED + "No movies found.")
        return

    for i in range(len(movie_list)):

        movie_name = movie_list[i][0]
        movie_rating = movie_list[i][1]

        print(
            Fore.CYAN +
            f"{i+1}. {movie_name}"
        )

        print(
            Fore.MAGENTA +
            f" Idmb Rating: {movie_rating}"
        )

def main():

    print(
        Fore.BLUE +
        "====================="
    )

    print(
        Fore.BLUE + 
        "MOVIE RECCOMENDATION SYSTEM"
    )

    print(
        Fore.BLUE +
        "=================="
    )

    name = input(Fore.YELLOW + "/nEnter Your Name: ")

    print(Fore.GREEN + f"\nWelcome {name}!")

    while True:

        display_genres()

        genre = get_genre()

        rating = get_rating()

        processing_animation()

        recommendations = recommend_movies(
            genre,
            rating

        )

        display_movies(
            recommendations,name
        )

        choice = input(
            Fore.YELLOW + 
            "\nWould you like more reccommendations? (yes/no):"
        ).lower()

        if choice == "no":

            print(
                Fore.GREEN + 
                f"\nThank you for using thr movie Reccommendation System, {name}!"
            )

            break
main()
