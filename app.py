from utility.csv_util import get_list, append_file
from utility.main import add_movie,list_movies,search_by_title

"""
Milestone Project 1 : Movie Collection App

User Story:
    As a user I would like to be able to...
        1. Add new movies to my collection, so I can keep track of all my movies
        2. List all the movies in my collection, so I can see what I already have
        3. Find a movie by using the movie title, so I can locate a specific move when my collection grows
        
    I would also like this to be able to...(BONUS)
        1. Check to see which movies I have seen, so I can keep track of what movies I still have yet to watch
        2. Search for a movie using the directors or other attributes, so I can find my specific movie

    Implementation tasks
        - Decide where to store movies in code                              *in a csv file called movies.csv
        - Decide what data we want to store for each movie                  *title, directors, year, genre, etc
        - Show the user a menu and let them pick an option
        - Implement each requirement in turn, each as a separate function
        - Stop running the program when they type 'q' in the menu

    How Movies are stored:
        - Title: Name of Movie
        - Director(s): Name of who directed that movie, can be multiple
        - Year: What year was that movie produced
        - Genre(s): What genre does this movie fall into, can be multiple
        - Have Seen: If you have seen this movie or not
        - Date Seen:

"""


print("Welcome to your Movie Collection Library!!!\n")

prompt = '\nWhat would you want to do?\n' \
         'add: adds movie to your current collection\n' \
         'list: gives a list of all movies in your collection\n' \
         'search: searches for a movie based on the title\n' \

while True:
    movie_collection = get_list()

    operation = input(prompt)
    if operation == 'q':
        print("\nGood bye!")
        break

    elif operation.lower() == 'add':
        append_file(add_movie(movie_collection))

    elif operation.lower() == 'list':
        list_movies(movie_collection)

    elif operation.lower() == 'search':
        movie_title = input("What is the movie title your searching for?: ")
        search_by_title(movie_collection, movie_title)