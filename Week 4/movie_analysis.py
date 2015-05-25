

def mov():
    infile = open('movies.txt','r')
    filelist = infile.read()
    infile.close()

    movie_info = filelist.split('\n')
    
    actors = []
    moviedict={}
    movielist = []
    movieinform = []

    for i in movie_info:

        i = i.replace('  ',' ')
        movieinform.append(i.split(', '))
        actors.append(movieinform[0])
        
    print actors
    print movieinform

    
##    movielist1 = [item for sublist in movielist for item in sublist]
##    movielist2 = set(movielist1)
##    movielist3 = []
##    movielist3.extend(movielist2)
##
##    print movielist2
##    print '---------------------------------------------------------'
##    print movielist3
##    print '---------------------------------------------------------'
##    print actors



    
##    for i in movie_info:
##        for j in movielist3:
##            for k in actors:
##                if j and k in i:
##                    moviedict[j] = k
##    print moviedict
                    
            
        
    

    
## actorlist = i.split(',')
##        actor = actorlist.pop(0)
##        actors.append(actor)
