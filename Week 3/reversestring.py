def reverse_v1(mystring):
    result=''
    
    for c in mystring:
        result=c+result

    print result
    return None


def reverse_v2(mystring):
    result=''
    
    for c in mystring:
        result=c+result

    return result

def reverseprint(mystring):
    '''reverse s and then print each character of the reversed string\n 
on a new line'''

    #which version of the reverse function should we use?
    
    reverse_string = reverse_v2(mystring)
    for letter in reverse_string:
        print letter
       
    return None

mystring = raw_input('input:  ') #need to define mystring
    
#I chose reverse_v2 because it takes each character in mystring and adds it
#to the back of the string. It then returns the result so that the next
#time it goes through the loop it will add onto the characters already
#added.
#In other words, version 2 allows the object result to be iterable.
#Version one does not work with the 
