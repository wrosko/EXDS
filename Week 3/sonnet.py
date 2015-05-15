'''
'''


def text(): #textanalysis(File):

    infile = open('sonnet.txt','r')
    line = infile.read()
    infile.close()
    
    LIST = []
    bigwordlist = line.split('\n')
    for c in bigwordlist:
        bigwordlist1= list(c.split(' '))
        LIST.append(bigwordlist1)
    #print bigwordlist

##    
##    for a in LIST:
##        for b in a:
##            if b =='':
##                del b
##            if b.isalpha():
##                pass
##            else:
##                print b
##                
    #print LIST
    LIST2= [item for sublist in LIST for item in sublist]
    LIST3 = []
    #print LIST2
    for c in LIST2:
        if c != '':
            LIST3.append(c)
    #print LIST3
    LIST4=[]
    for a in LIST3:
        for char in a:
            if char.isalpha():
                LIST4.append(a)
            else:
                a.replace(char,' ')
                LIST4.append(a)
    print LIST4







    #print bigwordlist1
##    for c in line:
##        if c = '':
##            pass
##        elif c.isalpha():
##            pass
##        else:
            
            
            
            

    
