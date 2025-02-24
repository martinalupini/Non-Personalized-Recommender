__author__ = 'Martina Lupini'

from Retriever import *
from Ranker import *
from PrintUtils import *
import os


def main():
    # First are the movies and associated rating are retrieved from the files movies.dat and ratings.dat
    num_users = retrieve_user_number()
    movies_dict = retrieve_movies()
    retrieve_ratings(movies_dict)

    ranker = Ranker(movies_dict)

    while(1):
        print("\n\nSelect your option:\n" +
            "[1] Calculate simple product association rule\n" +
            "[2] Calculate advanced product association rule\n" +
            "[3] Calculate top N movies with highest simple product association value\n" +
            "[4] Calculate top N movies with highest advanced product association value\n" +
            "[5] Calculate top N rated movies\n" +
            "[6] Calculate top N rated movies based on 4 star reviews\n" +
            "[7] Get info about movie from its ID\n" +
            "[8] Exit\n")
        choice = int(input("Insert chioce (1-8): "))

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

            value = ranker.advanced_product_association(movie_id1, movie_id2, num_users)
            print(value)

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

            top_N_dict = ranker.top_N_advanced_product_association(movie_id, N, num_users)
            print_dictionary_association(top_N_dict, movies_dict)

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

            top_N_dict = ranker.top_N_rated_movies(N, False)
            print_top_N_ranked(top_N_dict)

        elif choice == 6:

            while True:
                try:
                    N = int(input("Insert N: "))
                    if N > 0 and N < len(movies_dict):
                        break  # Exit loop once a valid ID is entered
                    else:
                        print("Invalid N (too large or negative)! Please try again.")
                except ValueError:
                    print("Invalid input! Please enter number.")

            top_N_dict = ranker.top_N_rated_movies(N, True)
            print_top_N_ranked(top_N_dict)

        elif choice == 7:
            while True:
                try:
                    movie_id = input("Insert movie ID: ")
                    if movie_id in movies_dict:
                        break  # Exit loop once a valid ID is entered
                    else:
                        print("Invalid movie ID! Please try again.")
                except ValueError:
                    print("Invalid input! Please enter a numeric movie ID.")

            print_movie_info(movies_dict[movie_id])

        elif choice == 8:
            exit()

        else:
            print("Invalid input! Please try again.")


if __name__ == "__main__":
    main()