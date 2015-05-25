def compare_movies(movie1, movie2):
    '''
    Compares two movies in terms of the actors in the two movies.
    Prints error message if one of the selected movies is not in the data file.
    Prints all of the actors who are in one or both of the movies.
    Prints all of the actors who are common to both movies.
    Prints all of the actors who are in one of the two movies but not both.
    '''
    # allows the program to recognize a movie even if entered in lowercase
    movie1 = movie1.lower()
    movie2 = movie2.lower()

##    # prints an error message if one of the selected movies is not in the file
##    if movie1 not in ???:
##        print movie1 'is not in the datafile'
##        movie1 = raw_input('Please select another movie: ')
##    if movie2 not in ???:
##        print movie2 'is not in the datafile'
##        movie2 = raw_input('Please select another movie: ')
##
##    # prints all of the actors who are in one or both movies
##
##    # return a new set with actors from the movie1 and movie2
##    union(other,...)
##
##    # prints all of the actors who are common to both movies
##
##    #return a new set with actors common to movie1 and movie2
##    intersection(other,...)
##    frozenset('abc').intersection('cbs')
##    # prints all of the actors who are in one of the two movies but not both
##
##    # return a new set with actors in either movie1 or movie2 but not both
##    symmetric_difference(other)

    return None

def coactors(actor):
    '''
    Prints error message if selected actor is not in the data file.
    Prints all of the selected actor's co-actors, i.e., all actors who appeared
    in a movie with the selected actor.
    '''

    return None


# Startup dialogue asking the user to select one of three options:
# compare movies, coactors, or quit (end the program).
def movieanalysis():
    '''
    Prompts user to select an option. Asks the user to input the appropriate
    information. Calls the appropriate function.
    '''

    movie_database = [] # creates an empty list
    movie_database = open('movies.txt').readlines() # makes each row a list

    for line in movie_database:
        actor = line.split(',')[:1] # list with just actor's name
        movies = line.split(',')[1:] # list with actor's movies
        # separates out the actor and his or her movies

    moviedict = {} # creates an empty dictionary to add movies and actors to
    for movie in movies:
        if movie in moviedict:
            moviedict[movie] = moviedict[movie].union(set(actor))
        else:
            moviedict[movie] = set(actor)

    print moviedict
    
    # create a set of actors for each of the movies in the data file

    # keys are movie titles
    # values are sets, composed of the actors in each movie
    

##    while True:
##        print 'Please choose one of the following options?: '
##        print ''
##        action = raw_input('compare movies (to compare the actors in two movies)\n \
##                            coactors (to find the coactors of a given actor) \n \
##                            quit (to quit the program): ')
##        print ''
##        if action == 'compare movies':
##            movie1 = raw_input('Enter name of first movie: ')
##            movie2 = raw_input('Enter name of second movie: ')
##            comapre_movies(movie1, movie2)

    return None
