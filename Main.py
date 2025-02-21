__author__ = 'Martina Lupini'

from Retriever import *
from Ranker import *
import os


def main():
    # First are the movies and associated rating are retrieved from the files movies.dat and ratings.dat
    movies_dict = retrieve_movies()
    retrieve_ratings(movies_dict)

    ranker = Ranker(movies_dict)

    while(1):
        print("Select your option:\n" +
            "[1] Calculate simple association rule\n" +
            "[2] Calculate advanced association rule\n" +
            "[3] Calculate top N movies with highest simple association value\n" +
            "[4] Calculate top N movies with highest advanced association value\n" +
            "[5] Calculate top N rated movies\n" +
            "[6] Get info about movie from its ID\n")
        choice = int(input("Insert chioce (1-5): "))

        if choice == 1:
            while True:
                try:
                    movie_id1 = input("Insert first movie ID: ")
                    if movie_id1 in movies_dict:
                        break  # Exit loop once a valid ID is entered
                    else:
                        print("Invalid movie ID! Please try again.")
                except ValueError:
                    print("Invalid input! Please enter a numeric movie ID.")

            while True:
                try:
                    movie_id2 = input("Insert second movie ID: ")
                    if movie_id2 in movies_dict and movie_id1 != movie_id2:
                        break  # Exit loop once a valid ID is entered
                    else:
                        print("Invalid movie ID! Please try again.")
                except ValueError:
                    print("Invalid input! Please enter a numeric movie ID.")

            value, _, _ = ranker.simple_product_association(movie_id1, movie_id2)
            print(value)
            os.system('cls')


        elif choice == 2:
            while True:
                try:
                    movie_id1 = input("Insert first movie ID: ")
                    if movie_id1 in movies_dict:
                        break  # Exit loop once a valid ID is entered
                    else:
                        print("Invalid movie ID! Please try again.")
                except ValueError:
                    print("Invalid input! Please enter a numeric movie ID.")

            while True:
                try:
                    movie_id2 = input("Insert second movie ID: ")
                    if movie_id2 in movies_dict and movie_id1 != movie_id2:
                        break  # Exit loop once a valid ID is entered
                    else:
                        print("Invalid movie ID! Please try again.")
                except ValueError:
                    print("Invalid input! Please enter a numeric movie ID.")

            value= ranker.advanced_product_association(movie_id1, movie_id2)
            print(value)
            os.system('cls')

        elif choice == 3:
            while True:
                try:
                    movie_id = input("Insert movie ID: ")
                    if movie_id in movies_dict:
                        break  # Exit loop once a valid ID is entered
                    else:
                        print("Invalid movie ID! Please try again.")
                except ValueError:
                    print("Invalid input! Please enter a numeric movie ID.")

            while True:
                try:
                    N = int(input("Insert N: "))
                    if N > 0 and N < len(movies_dict):
                        break  # Exit loop once a valid ID is entered
                    else:
                        print("Invalid N (too large or negative)! Please try again.")
                except ValueError:
                    print("Invalid input! Please enter number.")

            top_N_dict = ranker.top_N_simple_product_association(movie_id, N)
            print_dictionary_association(top_N_dict, movies_dict)
            os.system('cls')


        elif choice == 4:
            while True:
                try:
                    movie_id = input("Insert movie ID: ")
                    if movie_id in movies_dict:
                        break  # Exit loop once a valid ID is entered
                    else:
                        print("Invalid movie ID! Please try again.")
                except ValueError:
                    print("Invalid input! Please enter a numeric movie ID.")

            while True:
                try:
                    N = int(input("Insert N: "))
                    if N > 0 and N < len(movies_dict):
                        break  # Exit loop once a valid ID is entered
                    else:
                        print("Invalid N (too large or negative)! Please try again.")
                except ValueError:
                    print("Invalid input! Please enter number.")

            top_N_dict = ranker.top_N_advanced_product_association(movie_id, N)
            print_dictionary_association(top_N_dict, movies_dict)
            os.system('cls')

        elif choice == 5:

            while True:
                try:
                    N = int(input("Insert N: "))
                    if N > 0 and N < len(movies_dict):
                        break  # Exit loop once a valid ID is entered
                    else:
                        print("Invalid N (too large or negative)! Please try again.")
                except ValueError:
                    print("Invalid input! Please enter number.")

            top_N_dict = ranker.top_N_rated_movies(N)
            print_top_N_ranked(top_N_dict)
            os.system('cls')

        elif choice == 6:
            while True:
                try:
                    movie_id = input("Insert movie ID: ")
                    if movie_id in movies_dict:
                        break  # Exit loop once a valid ID is entered
                    else:
                        print("Invalid movie ID! Please try again.")
                except ValueError:
                    print("Invalid input! Please enter a numeric movie ID.")

            print(movies_dict[movie_id])

        else:
            print("Invalid input! Please try again.")


def print_dictionary_association(top_N_dict, movies_dict):
    i = 1
    for key, value in top_N_dict.items():
        print(str(i) + ". " + "Movie ID: " + key + " Movie Title: " + movies_dict.get(key)["Title"] + " Association Value: " + str(value) + "\n")
        i += 1


def print_top_N_ranked(top_N_dict):
    i = 1
    for key in top_N_dict.items():
        print(str(i) + ". " + "Movie ID: " + key + " Movie Title: " + top_N_dict.get(key)["Title"] + " # Users who rated: " + str(top_N_dict.get(key)["Frequency"]) + "\n")
        i += 1


if __name__ == "__main__":
    main()