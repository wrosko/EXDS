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

    reverse_string=reverse_v2(mystring)
    for letter in reverse_string:
        print letter
       
    return None

reverseprint(mystring)

mystring = raw_input("Please enter a string: ")
print reverseprint(mystring)

inputstring=raw_input("Please enter a string: ")
print reverseprint(inputstring)

