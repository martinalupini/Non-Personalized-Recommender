# Non-Personalized Recommender System

# Assignment 1: Non-Personalized Recommender System

The aim of this assignment is to implement a non-personalized recommender system based on product association rules. The dataset is divided into three parts:

- `Ratings.dat` contains information regarding the ratings of the movies.
- `Movies.dat` contains information regarding the movies.
- `Users.dat` contains information regarding the users.

## How to use the code

To use the code, unzip the `.zip` file and open a command line. Then launch `main.py` and a command line interface will appear. It is possible to choose between different options.

## Structure of the code

The code is written in [Python](https://www.python.org/) and it is organized in different classes. We will now comment on each one of them.

- `Main.py` contains the main method and the code for the command line interface.
- `PrintUtils.py` is a collection of print methods used in `main.py`
- `Retriever.py` contains the methods to collect the data from the file. In particular:
    - The method `retrieve_movies` reads the data from `movie.dat` file. All the data is saved into a nested dictionary. The movies are represented through a dictionary with the following keys (and of course the related values): `Title`, `Users` (list of users who rated the movie), `Frequency` (total number of ratings), `Users_4_star` (total number of ratings with 4 stars). Then all the movies are inserted into another dictionary with key `ID` of the movie and the dictionary described above as the value. The choice of this data structure is because it allows a fast retrieval of the information regarding a film simply by accessing its ID.
    - The method `retrieve_ratings` reads the data from the file `users.dat`. For each rating, it adds the user ID to the `Users` list of the corresponding movie.
    - The method `retrieve_user_number` reads the data from `users.dat` to obtain the total number of users.

- `Raker.py` contains the code that does the computation.
    - `Simple_product_association` computes the simple product association value between two movies.
    - `Advanced_product_association` computes the advanced product association value between two movies.
    - `Top_N_simple_product_association` returns the top N movies with the highest simple association value with the given movie.
    - `Top_N_advanced_product_association` returns the top N movies with the highest advanced association value with the given movie.
    - `Top_N_rated_movies` returns the top N movies with the most number of ratings (if the parameter `is_4_star` is set to `False`) or the top N movies with the most number of 4-star ratings.

----
Universiteit Gent, March 2025, Author: Martina Lupini