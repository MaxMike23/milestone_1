

def add_movie(movie_collection: list) -> dict:
    movie_entry = dict()

    movie_entry['Title'] = input('\nEnter the movie title: ')

    print('\nSearching for existing title...')
    for movie in movie_collection:
        if movie_entry['Title'] == movie['Title']:
            print('Movie already exists in collection\n')
            break

    movie_entry['Director(s)'] = input('\nEnter the director of this movie ("," for multiple directors): ').strip(" ")
    movie_entry['Director(s)'] = set(movie_entry['Director(s)'].split(','))

    movie_entry['Year'] = input('\nEnter the year of the movie: ')

    movie_entry['Genre(s)'] = input('\nEnter the genre for this movie ("," for multiple genres): ').strip(" ")
    movie_entry['Genre(s)'] = set(movie_entry['Genre(s)'].split(','))

    for key, value in movie_entry.items():
        if type(value) == set:
            value = ','.join(value)
        print(f"For {key} we have {value}")

    option = input('\nIs this correct? (y/n): ')
    if option.lower() == 'n':
        print("Please select 'add' and enter again\n")
    elif option.lower() == 'y':
        return movie_entry


def list_movies(movie_collection: list) -> None:
    for movie in movie_collection:
        print(f"{movie['Title']}, came out {movie['Year']}")


def search_by_title(movie_collection: list, movie_title: str) -> None:
    for movie in movie_collection:
        if movie_title == movie['Title']:
            print("\nMovie Found!")
            print(f"{movie['Title']}, came out {movie['Year']}\nDirected by {movie['Director(s)']}")
            break
        else:
            print("\nMovie not found in collection...")


def search_by(): #BONUS
    pass


def has_seen(): #BONUS
    pass