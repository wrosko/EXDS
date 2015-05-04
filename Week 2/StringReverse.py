def reverse(s):
    result = ""
    for c in s:
        result = c + result
    return result
t = raw_input("Please enter a string: ")
print 'The reverse of', t, ' is ', reverse(t)
