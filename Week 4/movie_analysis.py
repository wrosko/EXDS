

def mov():
    infile = open('movies.txt','r')
    filelist = infile.read()
    infile.close()

    movie_info = filelist.split('\n')
    
    actors = []
    moviedict={}
    movielist = []
    for i in movie_info:

        mv_info_list = i.split(',')
        
        actor = mv_info_list.pop(0)
        actors.append(actor)
        
        movies = mv_info_list[1:]
        movielist.append(movies)

    
    movielist1 = [item for sublist in movielist for item in sublist]
    movielist2 = set(movielist1)
    movielist3 = []
    movielist3.extend(movielist2)

    print movielist2
    print '---------------------------------------------------------'
    print movielist3


    for i in movie_info:
        for j in movielist3:
            if j in 
        
    

    
## actorlist = i.split(',')
##        actor = actorlist.pop(0)
##        actors.append(actor)
