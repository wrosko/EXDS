def reverse_v1(s):
    result=''
    
    for c in s:
        result=c+result

    print result
    return None


def reverse_v2(s):
    result=''
    
    for c in s:
        result=c+result

    return result

def reverseprint(mystring):
    '''reverse s and then print each character of the reversed string\n 
on a new line'''
    s = raw_input('input: ')
    #which version of the reverse function should we use?
    
    reverse_string=reverse_v2(mystring)
    for letter in reverse_string:
        print letter
       
    return None
#neither function works with the given variables because reverseprint tries
#to use the variable mystring. We have not defined the variable mystring.

#I chose reverse_v2 because it takes each character in s and adds it
#to the back of the string. It then returns the result so that the next
#time it goes through the loop it will add onto the characters already
#added.
#In other words, version 2 allows the object result to be iterable.
#Version 1 would not work because return None woudl cause the object to
#not be iterable.
