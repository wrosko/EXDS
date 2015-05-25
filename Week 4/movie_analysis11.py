import string
import re


def dic():
    infile = open('movies.txt','r')
    filelist = infile.readlines()
    infile.close()

    movie_info = filelist
    global actors
    global movies
    #global movies
    actors = []
    moviedict={}
    movielist = []
    

    #We got help from Nicol on how to use sets in this part so we can use
    #set commands later.
    for i in movie_info:
        i = i.strip('\n')
        i = i.replace('  ',' ')
        i = i.split(', ')
        
        actorsmovies = i[1:]
        actors.append(i[0])
        movielist.append(actorsmovies)
        
        for j in actorsmovies:
            if j not in moviedict:
                movieset = set()
                movieset.add(i[0])
                moviedict[j] = movieset
            else:
                movieset = moviedict[j]
                movieset.add(i[0])
                moviedict[j] = movieset          
    movies = moviedict.keys()
    print actors
    print movielist
    return moviedict


def movieinput():
    comparing = False
    while comparing == False:
        title = raw_input('Movie title:   ')
        title = string.capwords(title)
        if title == "You Have Got Mail":
            title = title[0] + title[1:].lower()
        if 'And' in title:
            title = title.replace('And', '&')
        if title in movies:
            return title
            comparing = True
            break
        else:
            print 'ERROR, the movie you entered is not in the text file'
            break
    return title
    

def comp(): #compare_movies():
    
    '''
    Compares two movies in terms of the actors in the two movies.
    Prints error message if one of the selected movies is not in the data file.
    Prints all of the actors who are in one or both of the movies.
    Prints all of the actors who are common to both movies.
    Prints all of the actors who are in one of the two movies but not both.
    '''


    print 'Please input the title of the first movie'
    movie1 = movieinput()
    print
    print 'Please input the title of the second movie'
    movie2 = movieinput()
    
    
            





##        if 'and' in movie1:
##            movie1.replace('and', '&')
##            
##        return movie1
    
    # allows the program to recognize a movie even if entered in lowercase
##    movie1 = movie1.lower()
##    movie2 = movie2.lower()

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

   # return None
    
