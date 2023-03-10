import requests, json


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMjZhODFmNThmZDI2YWNjMjg5Yjc0YzgyYzFmNGFiMiIsInN1YiI6IjY0MGIzNTE1MzI2ZWMxMDBjNGMwNWQ2NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.piMU7USiMJ1870vadcvmGJyJnJldkVeqzyx2d0_rbnE"
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()


response = get_popular_movies()
movies = response["results"]
# for movie in movies:
#    print(movie["title"])


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size.strip()}/{poster_api_path}"


def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]
