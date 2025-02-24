def print_dictionary_association(top_N_dict, movies_dict):
    i = 1
    for key, value in top_N_dict.items():
        print(str(i) + ". " + "Movie ID: " + key + "\nMovie Title: " + movies_dict.get(key)["Title"] + "\nAssociation Value: " + str(value) + "\n--------------------------------------------------------------------------------\n")
        i += 1


def print_top_N_ranked(top_N_dict):
    i = 1
    for key, value in top_N_dict.items():
        print(str(i) + ". " + "Movie ID: " + key + "\nMovie Title: " + top_N_dict.get(key)["Title"] + "\n# Users who rated: " + str(top_N_dict.get(key)["Frequency"]) + "\n--------------------------------------------------------------------------------\n")
        i += 1


def print_movie_info(movie):
    print("Movie Title:" + movie["Title"] + " Movie Genre: " + str(movie["Genre"]) + "\n" )