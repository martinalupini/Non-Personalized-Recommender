def retrieve_movies():
    movies_dict = {}
    with open("dataset/movies.dat", "r") as file:
        for line in file:
            parts = line.strip().split("::")
            if len(parts) == 3:
                movie_id, title, genres = parts
                genres = genres.split('|')
                movies_dict[movie_id] = {"Title": title, "Genres": genres, "Users" : [], "Frequency" : 0}
    return movies_dict


def retrieve_ratings(movies_dict):
    with open("dataset/ratings.dat", "r") as file:
        for line in file:
            parts = line.strip().split("::")
            if len(parts) == 4:
                movie_id, user_id, rating, timestamp = parts
                if movie_id in movies_dict:
                    movies_dict[movie_id]["Users"].append(user_id)
                    movies_dict[movie_id]["Frequency"] += 1