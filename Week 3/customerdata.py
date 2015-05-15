'''
'''
import random
import collections

#state is key, number is entry
def state(): #change to state_distribution()
    '''
    state_distribution imports and reads FakeCustomerData.txt.
    It stores each row of the document as a text file, then removes the
    first line which is the title of each data column, and the last row
    which is blank. Titles are stor
    '''
    infile = open('FakeCustomerData.txt','r')
    fileList = infile.read()
    customerdata = fileList.split('\n')#makes each row an entry
    del customerdata[-1]#deletes the blank line at end of document.
    customerdata.pop(0) #removes titles from list and returns them
    #customerlist=customerdata.remove()
    infile.close()
    #titles =list(titles_.split(','))#assigns removed titles to list
    #customersinfo = customerdata.split(',')
    state =[]#empty list where states will go
    stateDict ={} #establishes dictionary
    for i in customerdata:
        statecol = list(i.split(','))[7]#looks at the 8th object in each line which is the state
        #number_ = list(i.split(','))[0]#first object"number" of each line
        state.append(statecol) 
        if statecol in stateDict:
            stateDict[statecol]=stateDict[statecol]+1
        else:
            stateDict[statecol]=1
    orderedstate = collections.OrderedDict(sorted(stateDict.items()))#found this online

        #number.append(number_)
    #print titles_
    #print titles
    x = orderedstate.keys()
    y = orderedstate.values()
    z = zip(x,y)
    for k in z:
        print k
    #print number


def birth():
    '''
    '''
    infile = open('FakeCustomerData.txt','r')
    fileList = infile.read()
    customerdata = fileList.split('\n')
    del customerdata[-1]
    titles_ = customerdata.pop(0)


    infile.close()
    titles = list(titles_.split(','))
    birth = []
    birthdict = {}
    for i in customerdata:
        birthcol = list(i.split(','))[13]
        birth.append(birthcol)
    birthyr = []
    for j in birth:
        birthyear = list(j.split('/'))
        birthyr.append(birthyear)
        
##    birthyr = map(int(birthyr),birthyr) #maps the strign numbers to ints
    for k in birthyr:
        if k[2] in birthdict:
            birthdict[k[2]] = birthdict[k[2]]+1
        else:
            birthdict[k[2]] = 1
    orderedyr = collections.OrderedDict(sorted(birthdict.items()))

    keys = orderedyr.keys()
    values = orderedyr.values()
    zipped = zip(keys,values)
    for a in zipped:
        print a



















##
##
##def birth():
##    '''
##    '''
##    infile = open('fakecustomer.txt','r')
##    fileList = infile.read()
##    customerdata = fileList.split('\n')
##    del customerdata[-1]
##    titles_ = customerdata.pop(0)
##
##    infile.close()
##    titles = list(titles_.split(','))
##    birth = []
##    birthdict = {}
##    for i in customerdata:
##        birthcol = list(i.split(','))[13]
##        birth.append(birthcol)
##        for j in birthcol:
##            birthyear = list(j.split('/'))[2]
##            birth.append(birthyear)
##            if birthyear in birthdict:
##                birthdict[birthyear]=birthdict[birthyear]+1
##            else:
##                birthdict[birthyear]=1
##    print birthdict
##    for j in birth:
##        birthyear = list(j.split(','))
##        birth.append(birthyear)
##        
##        if birthyear in birthdict:
##            birthdict[birthyear]=birthdict[birthyear]+1
##        else:
##            birthdict[birthyear]=1
##    print birth
##        

    
            
    
    
    #eighth_column = fileList[1,:].split(',')[7]
    #print len(customerlist)
    #print customerlist
##    print titles
##    print
##    print customerdata
##    
    
##    for line in columns:
##        print line[7]

#create list for each customer, this gives us indexes. Create dictionary key
    #for each state. Assigned value is first entry of list
    #if key already exists, append value to dictionary
    
