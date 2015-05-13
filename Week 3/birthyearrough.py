


import collections

def birth():
    '''
    '''
    infile = open('fakecustomer.txt','r')
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
    
    print orderedyr

    keys = orderedyr.keys()
    values = orderedyr.values()
    zipped = zip(keys,values)
    for a in zipped:
        print a
        
































##def birth():
##    '''
##    '''
##    infile = open('birthyears.txt','r')
##    fileList = infile.read()
##    customerdata = fileList.split(',')
####    del customerdata[-1]
####    titles_ = customerdata.pop(0)
####
##    infile.close()
####    titles = list(titles_.split(','))
##    birth = 
##    birthdict = {}
##
##    for j in birth:
##        birthyear = list(j.split('/'))[2]
##        birth.append(birthyear)
##        if birthyear in birthdict:
##            birthdict[birthyear]=birthdict[birthyear]+1
##        else:
##            birthdict[birthyear]=1
##    print birth
##
##
##   
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
