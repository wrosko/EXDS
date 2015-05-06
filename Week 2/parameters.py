def isIn(x,y):
    if x in y:
        return True
    else:
        return False
x=raw_input('input a string for x: ')
y=raw_input('input a string for y: ')


if isIn(x,y)==True:
    print 'the first string is in the second'
else:
    print 'the first string is not in the second'
    
