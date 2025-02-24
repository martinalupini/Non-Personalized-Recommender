__author__ = 'Martina Lupini'

from itertools import islice


class Ranker:
    def __init__(self, movies_dict):
        self.movies_dict = movies_dict

    def simple_product_association(self, movieId_1, movieId_2):
        X = self.movies_dict[movieId_1]["Frequency"]
        X_and_Y = len(set(self.movies_dict[movieId_1]["Users"]) & set(self.movies_dict[movieId_2]["Users"]))
        if X ==0:
            res = 0
        else:
            res = X_and_Y/X
        return res, X_and_Y, X


    def advanced_product_association(self, movieId_1, movieId_2, num_users):
        simple_product_association, X_and_Y, X = self.simple_product_association(movieId_1, movieId_2)
        Y = self.movies_dict[movieId_2]["Frequency"]
        not_X_and_Y = Y - X_and_Y
        not_X = num_users - X
        if not_X_and_Y == 0 or not_X == 0:
            res = 0
        else:
            res = simple_product_association / (not_X_and_Y / not_X)
        return res


    def top_N_simple_product_association(self, movieId_1, N):
        dictionary = {}
        # Creating a new dictionary containing the movies id as key and their associations value has value
        for movieId in self.movies_dict:
            if movieId == movieId_1:
                continue
            value, _, _ = self.simple_product_association(movieId_1, movieId)
            dictionary[movieId] = value
        # Sorting the dictionary based on the association value
        ascending_id_dict = dict(sorted(dictionary.items(), reverse=True))
        sorted_dict = dict(sorted(ascending_id_dict.items(), key=lambda item: item[1], reverse=True))
        # Returning only the first N elements
        first_N_dict = dict(islice(sorted_dict.items(), N))
        return first_N_dict

    def top_N_advanced_product_association(self, movieId_1, N, num_users):
        dictionary = {}
        # Creating a new dictionary containing the movies id as key and their associations value has value
        for movieId in self.movies_dict:
            if movieId == movieId_1:
                continue
            dictionary[movieId] = self.advanced_product_association(movieId_1, movieId, num_users)
        # Sorting the dictionary based on the association value
        ascending_id_dict = dict(sorted(dictionary.items(), reverse=True))
        sorted_dict = dict(sorted(ascending_id_dict.items(), key=lambda item: item[1], reverse=True))
        # Returning only the first N elements
        first_N_dict = dict(islice(sorted_dict.items(), N))
        return first_N_dict


    def top_N_rated_movies(self, N, is_4_star):
        # Sorting the dictionary based on frequency of each movie
        ascending_id_dict = dict(sorted(self.movies_dict.items(), reverse=True))
        if is_4_star:
            sorted_dict = dict(sorted(ascending_id_dict.items(), key=lambda item: item[1]['Users_4_star'], reverse=True))
        else:
            sorted_dict = dict(sorted(ascending_id_dict.items(), key=lambda item: item[1]['Frequency'], reverse=True))
        # Returning the top N rated movies
        top_N_rated = dict(islice(sorted_dict.items(), N))
        return top_N_rated
