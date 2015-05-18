import myclass

def sign(integerpair):
    '''Receives an object of type MyClass and prints some information
about it.'''

    #Since integerpair is of type MyClass, we can use methods from that
    #class on this object
    if integerpair.mult() > 0:
        print 'both integers in pair are positive or both are negative'
    elif integerpair.mult() < 0:
        print 'one integer in pair is positive and the other negative'
    else:
        print 'at least one of the integers in pair is zero'

    return None

#to call on function remember the dot integerpairs = myclass.MyClass(2,3)
