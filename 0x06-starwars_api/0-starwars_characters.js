import requests
import sys

def get_movie_characters(movie_id):
    # Base URL of the Star Wars API
    base_url = "https://swapi.dev/api/films/"
    
    # Get the movie data
    response = requests.get(base_url + str(movie_id) + '/')
    if response.status_code != 200:
        print("Error: Unable to fetch data for the movie ID provided.")
        return
    
    movie_data = response.json()
    character_urls = movie_data['characters']
    
    # Fetch and print each character name
    for url in character_urls:
        character_response = requests.get(url)
        if character_response.status_code == 200:
            character_data = character_response.json()
            print(character_data['name'])
        else:
            print("Error: Unable to fetch character data from", url)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-starwars_characters.js <Movie ID>")
        sys.exit(1)
    
    movie_id = sys.argv[1]
    get_movie_characters(movie_id)