# this is the milestone project 1 
# the idea is to store movies from a user
# the user will be able to add a movie, find a movie, and list all movies

movies = []

menu = """
    SELECT AN OPTION
    1. add a movie
    2. print all movies
    3. find a movie

    'q' to terminate
"""
option = input(menu)

while (option != 'q'):
    if option == '1':
        movie = {}
        name = input('insert the title of the movie: ')
        director = input('insert the director: ')
        year = input('insert the release year: ')
        movie['name'] = name
        movie['director'] = director
        movie['year'] = year

        movies.append(movie)

    elif option == '2':
        for movie in movies:
            print(f"Name: {movie['name']}, Director: {movie['director']}, Year: {movie['year']}")

    else:
        name = input('insert the name of the movie to find: ')
        for movie in movies:
            if movie['name'].lower() == name.lower():
                print(f'Name: {movie["name"]}, Director: {movie["director"]}, Year: {movie["year"]}')
                break
        else:
            print('this movie is not listed, if you want you can add it')

    option = input(menu) 
