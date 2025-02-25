__author__ = 'Martina Lupini'

"""
This method return a nested dictionary containing the info about the films. The dictionary has the following structure:
{
movie_id : {Title: "title", Genres: "genres", Users: [], Users_4_star: 0, Frequency: 0}
}
"""
def retrieve_movies():
    movies_dict = {}
    with open("dataset/movies.dat", "r") as file:
        for line in file:
            parts = line.strip().split("::")
            if len(parts) == 3:
                movie_id, title, genres = parts
                genres = genres.split('|')
                movies_dict[movie_id] = {"Title": title, "Genres": genres, "Users" : [], "Users_4_star" : 0, "Frequency" : 0}
    # sorting the dictionary in descending key values
    movies_dict = dict(reversed(movies_dict.items()))
    return movies_dict


"""
This method adds the information about the rating to the movies saved in the dictionary data structure.
"""
def retrieve_ratings(movies_dict):
    with open("dataset/ratings.dat", "r") as file:
        for line in file:
            parts = line.strip().split("::")
            if len(parts) == 4:
                user_id, movie_id, rating, timestamp = parts
                if movie_id in movies_dict:
                    movies_dict[movie_id]["Users"].append(user_id)
                    movies_dict[movie_id]["Frequency"] += 1
                    if rating >= "4":
                        movies_dict[movie_id]["Users_4_star"] += 1



"""
This method return the total number of users who reviewed the films.
"""
def retrieve_user_number():
    num = 0
    with open("dataset/users.dat", "r") as file:
        for line in file:
            num += 1
    return num

