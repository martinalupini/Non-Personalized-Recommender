"""
This class contains method for printing the data structure in a more readable way.
"""


def print_dictionary_association(top_N_dict, movies_dict):
    i = 1
    for key, value in top_N_dict.items():
        print(str(i) + ". " + "Movie ID: " + key + "\nMovie Title: " + movies_dict.get(key)["Title"] + "\nGenres: " + str(movies_dict.get(key)["Genres"]) + "\nAssociation Value: " + str(value) + "\n--------------------------------------------------------------------------------")
        i += 1


def print_top_N_ranked(top_N_dict, is_4_Start):
    i = 1
    for key, value in top_N_dict.items():
        if is_4_Start:
            frequency = str(top_N_dict.get(key)["Users_4_star"])
        else:
            frequency = str(top_N_dict.get(key)["Frequency"])
        print(str(i) + ". " + "Movie ID: " + key + "\nMovie Title: " + top_N_dict.get(key)["Title"] + "\n# Users who rated: " + frequency + "\n--------------------------------------------------------------------------------")
        i += 1


def print_movie_info(movie):
    print("Movie Title:" + movie["Title"] + " Movie Genre: " + str(movie["Genres"]) + "\n" )