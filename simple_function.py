# Create a simple function called favorite_movie,
# which takes a string containing the name of your favorite movie.
# The function should then print “My favorite movie is named {name}”.

def favorite_movie (name):
    string_movie = f'My favorite movie is named {name}'
    return print(string_movie)

favorite_movie(name = (input('What is the name of your favorite movie?')).title())