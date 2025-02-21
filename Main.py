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
            "[5] Calculate top N rated movies\n")
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

            value, v, v2 = ranker.simple_product_association(movie_id1, movie_id2)
            print(value)
            os.system('cls')


        if choice == 2:
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




if __name__ == "__main__":
    main()