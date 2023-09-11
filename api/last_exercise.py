import requests
import requests_with_caching


def get_movies_from_tastedive(movie_name):
    base_url = "https://tastedive.com/api/similar"
    params = {
        "q": movie_name,
        "type": "movies",
        "limit": 5
    }
    response = requests_with_caching.get(base_url, params=params)
    movie_data = response.json()
    return movie_data


def extract_movie_titles(movie_dict):
    movie_list = movie_dict["Similar"]["Results"]
    movie_titles = [movie["Name"] for movie in movie_list]
    return movie_titles


def get_movie_data(movie_name):
    base_url = "http://www.omdbapi.com/"
    params = {
        "t": movie_name,
        "r": "json"
    }
    response = requests_with_caching.get(base_url, params=params)
    return response.json()


def get_movie_rating(omdb_dict):
    for rating in omdb_dict.get('Ratings', []):
        if rating['Source'] == 'Rotten Tomatoes':
            return int(rating['Value'][:-1])
    return 0


def get_sorted_recommendations(movie_titles_list):
    related_titles = []
    for title in movie_titles_list:
        related_titles.extend(extract_movie_titles(get_movies_from_tastedive(title)))

    # Remove duplicates from related_titles
    related_titles = list(set(related_titles))

    # Sort by Rotten Tomatoes rating and then by reverse alphabetical order
    # sorted_titles = sorted(related_titles, key=lambda title: (-get_movie_rating(get_movie_data(title)), title), reverse=True)
    sorted_titles = sorted(related_titles, key=lambda title: (-get_movie_rating(get_movie_data(title)), -ord(title[0])))
    return sorted_titles


# Uncomment for testing
print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"]))
