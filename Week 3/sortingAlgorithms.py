'''
File: sortingAlgorithms
Author: CS 1510
Description: This file gives sample implementations for three sorting
algorithms discussed in class: bubble sort, insertion sort, and
selection sort.

All of these sorting algorithms are big Oh value of n squared
'''

# Some lists to play with
ordered = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]

random = [75, 92, 57, 25, 31, 73, 30, 83, 88, 26, 2, 71, 22, 82, 22, 72, 70, 82, 14, 42]

shuffle = [8, 12, 11, 2, 15, 20, 16, 18, 17, 9, 3, 5, 1, 4, 10, 6, 14, 7, 13, 19]

doubleshuffle = [20, 22, 10, 32, 1, 4, 5, 14, 23, 13, 3, 31, 19, 7, 18, 40, 33, 25, 36, 35, 9, 11, 37, 6, 12, 38, 34, 26, 15, 21, 28, 8, 27, 17, 30, 24, 16, 29, 39, 2]

reverse = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

doublereverse = [40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def bubbleSort(lyst):

    compare=0   #Number of comparisons made
    swap=0      #Number of swaps made
    
    for aPass in range(len(lyst)):
        for index in range(len(lyst)-1):

            compare +=1
            if lyst[index]>lyst[index+1]:

                #Swapping the values at index and index+1
                temp = lyst[index]
                lyst[index] = lyst[index+1]
                lyst[index+1] = temp

                swap +=1
                
                #Python also lets you swap this way
                #lyst[index],lyst[index+1]=lyst[index+1],lyst[index]
                
    print ("comparisons "+str(compare))
    print ("swaps "+str(swap))   

 
def insertionSort(lyst):
    compare=0
    swap=0
    for j in range(1, len(lyst)):
        key = lyst[j]
        i = j - 1
        compare+=1
        while (i >=0) and (lyst[i] > key):
            lyst[i+1] = lyst[i]
            i = i - 1
            compare+=1
            swap+=1
        lyst[i+1] = key
    print ("comparisons "+str(compare))
    print ("swaps "+str(swap))

def selectionSort(lyst):
    compare=0
    swap=0
    for i in range(0, len(lyst)):
        min = i
        for j in range(i + 1, len(lyst)):
            compare+=1
            if lyst[j] < lyst[min]:
                min = j
        swap+=1
        lyst[i], lyst[min] = lyst[min], lyst[i] # swap
    print ("comparisons "+str(compare))
    print ("swaps "+str(swap))

