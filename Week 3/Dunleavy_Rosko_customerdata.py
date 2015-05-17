'''
File: Dunleavy_Rosko_customerdata.py
Authors: Dunleavy, Rosko
Description: Data analysis of the FakeCustomerData.txt file. Contains
    a function that lists the states, and number of customers from
    each state. Also contains a function that lists the birthyears
    of the customers and displays the number of customers with that
    birthyear.
'''
import random
import collections


def state_distribution():
    '''
    state_distribution imports and reads FakeCustomerData.txt.
    It stores each row of the document as an entry in a list, then removes the
    first entry which contains the title of each data column, and the last 
    entry which is blank. It then makes each entry in the customerdata list
    a list, and then calls on the entry related to the state. States are stored
    as keys in a dictionary, and the value is assigned by iterating through the
    state list. Prints the ordered dictionary for states, and number of
    customers in each state.
    '''
    infile = open('FakeCustomerData.txt','r')
    fileList = infile.read()
    customerdata = fileList.split('\n')#makes each row an entry
    del customerdata[-1]#deletes the blank line at end of document.
    customerdata.pop(0) #removes titles from list
    infile.close()
    
    state =[]#empty list where states will go
    stateDict ={} #establishes empty dicitonary that will be called on
    
    for i in customerdata:
        #Split each entry in customerdata, then access whichever
        #column of data by making each entry itself a list, and then
        #specify index 7 to call on the state entry.
        statecol = list(i.split(','))[7]
        state.append(statecol) #add each state to the state list
        
        #for each entry in state list, add state to dictionary and increase
        #its value by 1 if it is already in the dictionary
        if statecol in stateDict:
            stateDict[statecol]=stateDict[statecol]+1
        else:
            stateDict[statecol]=1
            
    #By using the built in collections module, create an ordered dictionary
    orderedstate = collections.OrderedDict(sorted(stateDict.items()))

    #Here we set the variables x and y equal to the keys and values
    #respectively.
    x = orderedstate.keys()
    y = orderedstate.values()

    #zip the two variables' lists and then print each pair
    z = zip(x,y)
    for k in z:
        print k
    #print number


def birth_year_distribution():
    '''
    birth_year_distribution imports and reads FakeCustomerData.txt.
    It stores each row of the document as an entry in a list, then removes the
    first entry which contains the title of each data column, and the last 
    entry which is blank. It then makes each entry in the customerdata list
    a list, and then calls on the entry related to the birthday. Each birthday
    is then an entry in birthcol. The birthyear is then separated from the
    birthday. A dictionary is created where birthyears are the keys and
    the number of customers with that birthyear are the values. These are both
    printed.
    '''
    infile = open('FakeCustomerData.txt','r')
    fileList = infile.read()
    customerdata = fileList.split('\n')#makes each row an entry
    del customerdata[-1]#deletes the blank line at end of document.
    customerdata.pop(0) #removes titles from list
    infile.close()
    
    birth = [] #empty list where the birthday with day/month/year are stored
    birthdict = {} #establishes empty dicitonary that will be called on
    
    for i in customerdata:
        #Split each entry in customerdata, then access whichever
        #column of data by making each entry itself a list, and then
        #specify index 13 to call on the birthday entry.
        birthcol = list(i.split(','))[13]
        birth.append(birthcol) #adds each birthday to the birth list
        
    birthyr = [] #create empty list for birthdays
    #take each entry in birth and turn it into a list separated by "/"
    
    for j in birth:
        birthyear = list(j.split('/'))
        birthyr.append(birthyear) #store each birthday entry as lists within
                                  #the list birthyr
        
    #For each entry in second index of birthyear, add year to dictionary and 
    #increase its value by 1 if it is already in the dictionary
    for k in birthyr:
        if k[2] in birthdict:
            birthdict[k[2]] = birthdict[k[2]]+1
        else:
            birthdict[k[2]] = 1
            
    #By using the built in collections module, create an ordered dictionary
    orderedyr = collections.OrderedDict(sorted(birthdict.items()))

    #Set the variables keys and values equal to the keys and values
    #respectively.
    keys = orderedyr.keys()
    values = orderedyr.values()

    #zip the two variables' lists and then print each pair
    zipped = zip(keys,values)
    for a in zipped:
        print a
        #Print birthyear and number of customers with that birthyear



















    
