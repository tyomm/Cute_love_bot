from googlesearch import search

def is_movie_site(url):
    movie_keywords = ["imdb.com", "rottentomatoes.com", "tmdb.org", "letterboxd.com", "films.bz", "https://lookmovie.foundation/"]  # Add more keywords as needed
    return any(keyword in url for keyword in movie_keywords)

def search_film(film_name):
    query = f"{film_name} movie"
    try:
        links = list(search(query, num=1, stop=1, pause=2))  # Adding pause to avoid being blocked
        if links:
            movie_links = [link for link in links if is_movie_site(link)]
            if movie_links:
                return movie_links[0]
            else:
                return None
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None



