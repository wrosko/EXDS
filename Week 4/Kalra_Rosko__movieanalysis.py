"""
File: Kalra_Rosko_movieanalysis.py
Authors: Kalra, Rosko
Description: Movie database analyzer that will set up a dictionary with movies
    as the keys, and sets of actors as the values. Based on two movies entered
    by a user, the program will output all of the actors in the two movies, the
    actors who are in both movies, and the actors who are in one movie but not
    the other. Additionally, the program is able to output an actors coactors.
"""

import string #import built in string module.


def dic():
    """
    dic() reads the file and stores each line of the file as an entry in a
    list. Establishes a dictionary, and two lists to be used to create the
    dictionary.
    """
    infile = open('movies.txt','r')
    filelist = infile.readlines()
    infile.close()
    movie_info = filelist #assign filelist as a variable

    #make actors and movies global, then establish the actor and movie list
    #lists, and make the moviedictionary.
    global actors
    global moviedict
    actors = []
    moviedict={}
    movielist = []
    

    #We got help from Nicol on how to use sets in this part so we can use
    #set commands later.
    
    #Take each entry in movie_info and strip \n's, split it into a list
    #separated by ",", and replace double spaces.
    for i in movie_info:
        i = i.strip('\n')
        i = i.replace('  ',' ')
        i = i.split(', ')
        #add movies to movie list and actors to actor list
        actorsmovies = i[1:]
        actors.append(i[0])
        movielist.append(actorsmovies)

        #for each entry in actorsmovies, use capword function from string
        #module to capitalize each word in the movie titles.
        for j in actorsmovies:
            j=string.capwords(j)

            #Set movies as the keys in the dictionary, and actors as values
            if j not in moviedict:
                movieset = set()
                movieset.add(i[0])
                moviedict[j] = movieset
            else:
                movieset = moviedict[j]
                movieset.add(i[0])
                moviedict[j] = movieset
    #create movie list from keys of dictionary, return the dictionary
    
    return moviedict


def movieinput():
    """
    movieinput()takes the raw input from the user for a movie name, and then
    capitalizes the first letter of every word. It also takes into account
    the anomolies in the movies.txt file like extra space, and making it so
    that if a user inputs "and", it will be changed to &. Will return the title
    of the movie.
    """
    title = raw_input('Movie title:   ')
    title = string.capwords(title) #with string module,capitalize first letters

    #take into account "and", and if the title is in the moviesdict.
    if 'And' in title:
        title = title.replace('And', '&')
        return title
    if title in moviedict:#See if title is in moviedict keys
        return title
    if title == None:
        print "ERROR, you didn't enter anything."
        return None
    else:
        print 'ERROR, the movie you entered is not in the file'
        return None
            

def actorinput():
    """
    actorinput() prompts the user for the name of an actor. It capitalizes
    the first letters of the actor's name. Checks to see if actor is a value
    of the dictionary.
    """
    actor = raw_input('Movie actor:   ')
    actor = string.capwords(actor) #capitalize first letter of every word
    
    if actor in actors:
        return actor
    if actor == None:
        print "ERROR, you didn't enter anything."
        return None
    else:
        print 'ERROR, the actor you entered is not in the file'
        return None
    
    

def compare(): #compare_movies():
    
    '''
    Compares two movies in terms of the actors in the two movies.
    Prints error message if one of the selected movies is not in the data file.
    Prints all of the actors who are in one or both of the movies.
    Prints all of the actors who are common to both movies.
    Prints all of the actors who are in one of the two movies but not both.
    '''

    #call on the movieinput() function twice, once for movie1 and once for
    #movie2.
    print 'Please input the title of the first movie'
    movie1 = movieinput() 
    print
    print 'Please input the title of the second movie'
    movie2 = movieinput()

    #if movieinput() returns none for either movie show error message.
    if movie1 == None:
        print 'There is nothing to compare'
    elif movie2 == None:
        print 'There is nothing to compare'

    #call on the dic() function to get the dictionary, and then get the values
    #of the dictionary with the get() command.
    else:
        movie1actors = dic().get(movie1)
        movie2actors = dic().get(movie2)
        
        #Use union, intersection, and symmetrical difference on the sets to
        #find the actors' relationships to the given movies.
        #list() command is used to remove the set(....) part from the printed
        #statement. It is merely for aesthetic pleasure.
        allactors = list(set(movie1actors) | set(movie2actors)) #union
        similaractors = list(set(movie1actors) & set(movie2actors))#intersection
        diffactors = list(set(movie1actors) ^ set(movie2actors))#symmetrical diff

        print 'All of the actors in the two named movies are:  ',allactors
        print 'The two movies share the following actors: ',similaractors
        print 'The actors who are in only one of the movies are: ',diffactors
    

def coactors():
    """
    coactors() uses results from the dictionary to find coactors of the actor
    entered by the user. Calls on the actorinput() function. Prints the actor's
    coactors.
    """
    
    print "Please input the actor's name."
    actor = actorinput()#call on actorinput() function
    actors = [] #empty list
    actorsdict = {} #empty dictionary
    if actor == None:
        print 'The actor was not in the file'
        print
    #for each key in dic(), get values. Then append those values to the
        #actor list
    else:
        for k in dic():
            values = list(dic().get(k))
            if actor in values:
                actors.append(values)
        actors = list(set([item for sublist in actors for item in sublist]))
        actors.remove(actor)
        actorsdict[actor] = actors #set actors1 as a dictionary with the actor
                                   #as the key, and coactors as values.
            
        print
        print actor+"'s coactors are: ",actorsdict.get(actor)#print dict value
        print
        
    
 

def movieanalysis():
    """
    movieanalysis() is the main function of the program. It will call on dic(),
    compare(), and coactors(). It prompts the user to input a, b, or c
    to choose betwen comparing movies, finding coactors, and quitting the
    program
    """
    dic()#Calls on dic()
    analysis = False
    while analysis == False:#Establsih a while loop
        print
        #Prompt for user input
        entry = raw_input('Hello! Welcome to the movie analyzer. please pick' \
                          ' an option. \n'
                          'a. "compare movies" to compare the actors in each.'\
                          '\n'
                          'b. "coactors" to find the coactors of an actor. \n'
                          'c. "quit" to quit the program.\n:').lower()
        print
        #depending on input, a different function will be called, or program
        #will quit.
        if entry.isalpha() and entry in ['a']:
            compare()
        elif entry.isalpha() and entry in ['b']:
            coactors()
        elif entry.isalpha() and entry in ['c']:
                print 'QUIT'
                analysis = True
        else:
            print 'Please choose a, b, or c'
            
        
                          
        

    
    
    
            
