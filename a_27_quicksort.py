#! /usr/bin/env python3

"""
This part use python3 write:
    QuickSort
"""

import random

def swap(data, i, j):
    if i==j:
        return
    else:
        if i>= len(data) or j>=len(data):
            print("{} or {} is greater than length of the sequence.".format(i,j,len(data)))
        else:
            data[i], data[j]=data[j],data[i]
            print(repr(data))

def partition(data, low, high):
    if low>=high:
        return low
    
    index=random.randrange(low, high);
    swap(data, low, index)

    middle=low
    for i in range(low, high+1):
        if data[low]>data[i]:
            middle=middle+1
            swap(data, middle, i)

    swap(data, low, middle)
    return middle

def quicksort(data, low, high):
    if low<high:
        middle=partition(data, low, high)
        print(repr([middle, low, high]))
        
        quicksort(data, low, middle-1)
        quicksort(data, middle+1, high)


sample=random.sample(range(100),20)
print("before sort:", repr(sample))
quicksort(sample, 0, len(sample)-1)
print("after sort:",repr(sample))








































































































































































































































































































































