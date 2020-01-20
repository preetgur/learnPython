"""
Author : Gurpreet singh
Date 20 jan 2020

############# Basic cmd

[np.fxn : generic fxn]

1. check the type of numpy dimension : ndim
ex. a.ndim

2. itemsize : tell about the size of each elements
ex. a.itemsize

3. a.dtype : Tells about the type of datatype/ or used to initialize array with specific datatype
ex. [ dtype = np.int32  , dtype = np.float64, dtype = complex]

4. a.size : tells about the total no of elements 

5. a.shape : tells about the no. of rows and coloums in array

6. np.zeros(shape) : initialize array with zeros with shape specified.
ex. one_matrix = np.ones((3,4))  #initialize with ones

7. np.arange() : similar to range in list 
# arange fxn :, but returns an ndarray rather than a list.

8. np.linspace(1,5,20) : Returns `num` evenly spaced samples, calculated over the interval [`start`, `stop`].
 
9. a.reshape() :  reshape to any dimensions

10. a.ravel() : flaten array : make any dimensional to one-dimensional array

##### Mathematical fxn

11. a.min() : returns minimum no in array

12. a.max() : 

13. a.sum() : adding all the elements in the array

14. a.sum(axis=0)   adding all the element in columns wise

15. a.sum(axis=1)   adding all the element in row wise

16. np.sqrt()   : calculate square root of each elements

17. np.std()  : calculate standard devaiation

18. a.dot(b)  : Matrix production of two array a and b
"""

import numpy as np

########## n dimensional numpy array

a = np.array([5,6,7])  #one dimensional numpy
print(a,type(a))

print("Value at Zero index : ",a[0])


# Two dimesinal array
a = np.array([ [1,2], [3,4], [5,6] ])
print(a,type(a))
print(f"#### {a.ndim} : Type of  dimensional : ")
print(f"#### size of each item/elements :{a.itemsize}   ")
print(f"#### Type of datatype :{a.dtype}   ")

# Initialize array with specific data-type :
a = np.array([ [1,2], [3,4],[5,9] ], dtype=np.float64)
print(f"#### Type of datatype :{a.dtype} and itemsize : {a.itemsize}   ")
print(a)

print(f"#### Total no of elements  :{a.size}   ")
print(f"#### No. of rows and coloums (row,colums) :{a.shape}   ")


#initialize array with zero : 3 row and 4 coloms
zero_matrix = np.zeros((3,4))
print(zero_matrix,zero_matrix.dtype)

# initialize with one : aloong with changed datatype
one_matrix = np.ones((3,4),dtype=np.int32)
print(one_matrix,one_matrix.dtype)


# arange fxn :, but returns an ndarray rather than a list.
 

rang = np.arange(1,5,2)
print("arange fxn : ",rang)


#Generate linearly numbers bw specified numbers :
# Returns `num` evenly spaced samples, calculated over the interval [`start`, `stop`].

linear_sep = np.linspace(1,5,20) 
# generate 10 numbers evenly spaced bw 1, 5
print(linear_sep)



# Reshape 

print(f"### Befor Reshape : {a.shape}\n {a}" )
reshp = a.reshape(2,3)
print(f"### After Reshape of array :\n {reshp}")
reshp = a.reshape(6,1)
print(f" Six row one colums : {reshp}")

# flaten array : convert n-dimensinal to one-dimensional
# returns a new array : You have to caputre that array using varible

print(f"Flaten array a : {a.ravel()}")


#### Mathematical fxn

print(f"Minimum no in array : {a.min()}")
print(f"Maximum no in array : {a.max()}")
print(f"Addtion of all the elements in array : {a.sum()}")

# axis 0 : means column wise
# axis 1 : means row wise
print(a)
print(f"Addtion of elements :Column wise : {a.sum(axis=0)}")
print(f"Addtion of elements :Row wise : {a.sum(axis=1)}")

print(f"Square root : {np.sqrt(a)}")

print(f"Standard devation : {np.std(a)}")


a = np.array([ [ 1,2], [3,4] ])
b = np.array([ [ 5,6], [7,8] ])
print(a,"\n",b)

print(f"Addtion : {a+b}")
print(f"Subtraction  : {a-b}")
print(f"Multiplication  : {a*b}")

### Matrix production :
print(f"Matrix Production  : \n{a.dot(b)}")



