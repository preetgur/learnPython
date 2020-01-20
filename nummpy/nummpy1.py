""" 
Author : Gurpreet Singh
Date : 20 Jan 2020
Purpose : Understand the concept of numpy.

####################
numpy : is heavily used in scientific computation

numpy's most useful features is n "dimentional array" object

########### Installing
>>>  pip install numpy

########### 3 Main Benfits of numpy over python list
1. Less Memory 
2. Fast 
3. Convinient

############ size 
*****size of one elemnt in list is : 14 bytes :{Because everything in pyton is an object, so the list will contains the "list of pointers" first and each pointer will points to other location in memory which will your object}

******size of one elemnt in numpy array  is : 4 bytes

"""

import numpy as np 
import time
import sys


print("######### Numpy takes less memory  ###########")
##### create numpy array   : similar to list

arr = np.array([1,3,9,5])
print(arr)


######### Create list

li = range(1000)           # created a list having 1000 object
print(f"**** size [length] of list : {len(li)}")
print(f"**** size of each items/element in  list : {sys.getsizeof(2)}")
print(sys.getsizeof(2)*len(li))    
#getsizeof -> int :Return the size of any list element in bytes.


######### Create numpy array

arr = np.arange(1000)
print(f"**** size of numpy array : {arr.size}")
print(f"**** size of each items in  numpy array : {arr.itemsize}")

print(arr.size*arr.itemsize)

# size of every element in arr : arr.itemsize
# size of array : array.size

print("######### Numpy array is fast and convinient compared to native python list  ###########")


# create two list and two numpy array and compare bw them

SIZE = 100000

l1 = range(SIZE)
l2 = range(SIZE)


a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

# Python list 
start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
print(f"Python list took {(time.time()-start)*1000}")


# Numpy array
start = time.time()
result = a1 + a2
print(f"Numpy array list took {(time.time()-start)*1000}")



# Simple Addtion : NO use of list comprehesnion as in case of list needed
a3 = np.array([1,2,3])
a4 = np.array([4,5,3])
print(f"Addtion of two numpy array : {a3+a4}")
