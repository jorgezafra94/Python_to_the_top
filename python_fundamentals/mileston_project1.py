# this is the milestone project 1 
# the idea is to store movies from a user
# the user will be able to add a movie, find a movie, and list all movies

movies = []

menu = """
    SELECT AN OPTION
    a - add a movie
    p - print all movies
    f - find a movie

    q - to terminate
"""
option = input(menu)

def add_mov():
    movie = {}
    name = input('insert the title of the movie: ')
    director = input('insert the director: ')
    year = input('insert the release year: ')
    movie['name'] = name
    movie['director'] = director
    movie['year'] = year

    movies.append(movie)


def print_mov():
    for movie in movies:
        print(f"Name: {movie['name']}, Director: {movie['director']}, Year: {movie['year']}")


def find_mov():
    name = input('insert the name of the movie to find: ')
    for movie in movies:
        if movie['name'].lower() == name.lower():
            print(f'Name: {movie["name"]}, Director: {movie["director"]}, Year: {movie["year"]}')
            break
    else:
        print('this movie is not listed, if you want you can add it')


options = {
    'a': add_mov,
    'p': print_mov,
    'f': find_mov
}


while (option != 'q'):       
    if option in options.keys():
        options[option]()
    else:
        print('please enter a valid option')
        
    option = input(menu) 
