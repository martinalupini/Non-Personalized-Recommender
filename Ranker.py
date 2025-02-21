from itertools import islice


class Ranker:
    def __init__(self, movies_dict):
        self.movies_dict = movies_dict

    def simple_product_association(self, movieId_1, movieId_2):
        X = self.movies_dict[movieId_1]["Frequency"]
        X_and_Y = len(set(self.movies_dict[movieId_1]["Users"]) & set(self.movies_dict[movieId_2]["Users"]))
        return X_and_Y / X, X_and_Y, X


    def advanced_product_association(self, movieId_1, movieId_2):
        simple_product_association, X_and_Y, X = self.simple_product_association(movieId_1, movieId_2)
        Y = self.movies_dict[movieId_2]["Frequency"]
        not_X_and_Y = Y - X_and_Y
        return simple_product_association / (not_X_and_Y / X)


    def top_N_simple_product_association(self, movieId_1, N):
        dictionary = {}
        # Creating a new dictionary containing the movies id as key and their associations value has value
        for movieId in self.movies_dict:
            if movieId == movieId_1:
                continue
            dictionary[movieId] = self.simple_product_association(movieId_1, movieId)
        # Sorting the dictionary based on the association value
        sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))
        # Returning only the first N elements
        first_N_dict = dict(islice(sorted_dict.items(), N))
        return first_N_dict

    def top_N_advanced_product_association(self, movieId_1, N):
        dictionary = {}
        # Creating a new dictionary containing the movies id as key and their associations value has value
        for movieId in self.movies_dict:
            if movieId == movieId_1:
                continue
            dictionary[movieId] = self.advanced_product_association(movieId_1, movieId)
        # Sorting the dictionary based on the association value
        sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))
        # Returning only the first N elements
        first_N_dict = dict(islice(sorted_dict.items(), N))
        return first_N_dict


    def top_N_rated_movies(self, N):
        # Sorting the dictionary based on frequence of each movie
        sorted_dict = dict(sorted(self.movies_dict.items(), key=lambda item: item[1]['Frequency']))
        # Returning the top N rated movies
        top_N_rated = dict(islice(sorted_dict.items(), N))
        return top_N_rated
