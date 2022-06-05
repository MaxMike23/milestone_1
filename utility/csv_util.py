from csv import reader, DictWriter


def get_list(csv_file: str = 'movies.csv') -> dict:

    # Movies will be stored as follows:
    #   [{'title': 'A Clockwork Orange', 'directors': {'Stanley Kubrick'}, 'year': 1971, 'genres': {'Crime', 'Sci-Fi'}}
    #   Note: Both the directors and genres are sets instead of strings because you can have multiples of each

    movie_collection = [] # Create an empty list to store movies

    with open(csv_file, 'r') as file:
        data = reader(file)     # stores the reader file in a variable
        next(data)              # Moves to the next line in the read csv file

        for movie in list(data):
            movie_dict = {
                'Title': movie[0],
                'Director(s)': set(movie[1].split('/')),
                'Year': movie[2],
                'Genre(s)': set(movie[3].split('/')),
            }
            movie_collection.append(movie_dict)

        file.close()

    return movie_collection


def append_file(movie: dict, csv_file: str = 'movies.csv') -> None:

    movie_headers = ['Title', 'Director(s)', 'Year', 'Genre(s)']

    movie_collection = get_list(csv_file)
    num_movies = len(movie_collection)

    with open(csv_file, 'a', newline='') as file:

        movie_exists = False
        for x in movie_collection:
            if movie['Title'] == x['Title']:
                print(f"{movie['Title']} is already in your current movie collection")
                movie_exists = True
                break

        movie['Director(s)'] = '/'.join(movie['Director(s)'])
        movie['Genre(s)'] = '/'.join(movie['Genre(s)'])

        if not movie_exists:
            dictwriter_object = DictWriter(file, fieldnames=movie_headers)
            dictwriter_object.writerow(movie)

        file.close()

        new_movie_collection = get_list(csv_file)
        if len(new_movie_collection) == len(movie_collection) + 1:
            print("\nNew movie added successfully!")
        else:
            print("\nSomething went wrong..")


