# Projeto 12
# Recomendações de filmes baseadas nas solicitações do usuário e no Rotten Tomatoes


import requests
import json

''' 
    It should take one input parameter, a string that is the name of a movie or music artist.
    The function should return the 5 TasteDive results that are associated with that string;
    be sure to only get movies, not other kinds of media.
'''


def get_movies_from_tastedive(movie_name):
    base_url = "https://tastedive.com/api/similar"
    params_dict = {}
    params_dict['q'] = movie_name
    params_dict['type'] = 'movies'
    params_dict['limit'] = 5
    tastedive_resp = requests.get(base_url, params=params_dict)
    return tastedive_resp.json()


''' 
    Function that extracts just the list of movie titles from a dictionary returned
    by get_movies_from_tastedive.
'''


def extract_movie_titles(movies_dict):
    movies_list = []
    for dictio in movies_dict['Similar']['Results']:
        movies_list.append(dictio['Name'])
    return movies_list


'''
    It takes a list of movie titles as input. It gets five related movies for
    each from TasteDive, extracts the titles for all of them, and combines
    them all into a single list. Don’t include the same movie twice.
'''


def get_related_titles(movies_list):
    related_list = []
    for movie in movies_list:
        movies_tastedive = get_movies_from_tastedive(movie)
        for dictio in movies_tastedive['Similar']['Results']:
            if dictio['Name'] not in related_list:
                related_list.append(dictio['Name'])
    return related_list


'''
    It takes in one parameter which is a string that should represent the title
    of a movie you want to search. The function should return a dictionary with
    information about that movie.
'''


def get_movie_data(movie_name):
    base_url = "http://www.omdbapi.com/?i=tt3896198&apikey=8c0f8708"
    params_dict = {}
    params_dict['t'] = movie_name
    params_dict['r'] = 'json'
    omdb_resp = requests.get(base_url, params=params_dict)
    return omdb_resp.json()


'''
    It takes an OMDB dictionary result for one movie and extracts
    the Rotten Tomatoes rating as an integer.
    For example, if given the OMDB dictionary for “Black Panther”, it would
    return 97. If there is no Rotten Tomatoes rating, return 0.
'''


def get_movie_rating(omdb_dict):
    num_grade = 0
    for dictio in omdb_dict["Ratings"]:
        if "Rotten Tomatoes" in dictio["Source"]:
            grade = dictio['Value']
            num_grade = int(grade[:-1])
    return num_grade


'''
    It takes a list of movie titles as an input. It returns a sorted list of
    related movie titles as output, up to five related movies for each input
    movie title.
    The movies should be sorted in descending order by their Rotten Tomatoes
    rating, as returned by the get_movie_rating function. Break ties in reverse
    alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.
'''


def get_sorted_recommendations(movies_list):
    prov_dict = {}
    lista = get_related_titles(movies_list)
    for movie in lista:
        prov_dict[movie] = get_movie_rating(get_movie_data(movie))
    sorted_list = sorted(prov_dict.keys(), key=lambda key: (
        prov_dict[key], key), reverse=True)
    # print(sorted_list)
    # print(prov_dict)
    return sorted_list
    # return sorted(lista, key = lambda x : (get_movie_rating(get_movie_data(x)), x), reverse = True)
    # return sorted(lista)


get_sorted_recommendations(["The greatest showman", "Iron-man"])
