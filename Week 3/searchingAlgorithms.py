'''
File: searchingAlgorithms.py
Author: CS 1510
Description: This file contains two search functions discussed in class:
linear search and binary search.  
'''

# Misc. lists to feed into the functions
ordered = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]

random = [75, 92, 57, 25, 31, 73, 30, 83, 88, 26, 2, 71, 22, 82, 22, 72, 70, 82, 14, 42]

shuffle = [8, 12, 11, 2, 15, 20, 16, 18, 17, 9, 3, 5, 1, 4, 10, 6, 14, 7, 13, 19]

doubleshuffle = [20, 22, 10, 32, 1, 4, 5, 14, 23, 13, 3, 31, 19, 7, 18, 40, 33, 25, 36, 35, 9, 11, 37, 6, 12, 38, 34, 26, 15, 21, 28, 8, 27, 17, 30, 24, 16, 29, 39, 2]

reverse = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

doublereverse = [40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


#linearSearch has a Big O value of n
def linearSearch(lyst,item):
    for index in range(len(lyst)):
        if lyst[index]==item:
            return index
    return -1

#binarySearch has a Big O value of log n
#Does the list need to be sorted for the binarySearch to work?
def binarySearch(lyst,item):
    low=0
    high=len(lyst)-1

    while low<=high:

        middle = (high+low)/2
        
        if lyst[middle]==item:
            return middle
        elif lyst[middle]>item:
            high=middle-1
        else:
            low=middle+1
    return -1
        
