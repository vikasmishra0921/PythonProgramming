#Array defination - 
# Array can store value of different data types.

lst = [1,2,3,4,5] #1 dimensional array
lst1= [[1,2,3]]   #2 dimensional array
lst2 =  [[[1,2,3,4,5]]] #3 dimensional array

# Rasterization -

# Turning on the pixel at a  specific intensity is called rasterization.
# Computer only understands 0 and 1 so they are true and false. So basically if we touch the screen then the pixel is on and if we don't touch it then the pixel is off and off is 0 and on is 1.

# So the computer will understand that the pixel is on or off. So this is called rasterization. This process is essential for rendering images on the screen.
# Numpy is a powerful library in Python that provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays. It is widely used in data science, machine learning, and scientific computing due to its efficiency and ease of use.
# The numpy is a vectorized form of Array that consumes less memory and less computational cost.
# It is used for numerical computation.
# Numerical computation means we can perform mathematical operations on the data.


#  Y is always a dependent column and X is always an independent column
# *Age column - X, salary column - Y
# There can be more than one independent column but the dependent column will remain one
# Y depends on x but x is independent
# There can be more than one independent column but the dependent column will remain one



#####################  lets start with the numpy library #####################


# Importing the numpy library

import numpy as np

#numpy --> Numerical Python
# np --> numpy

# Array Defination

lst = [10,20,30,40,50] # 1 dimensional array

print(type(lst)) # <class 'list'>

#Numpy array defination

arr = np.array(lst)

print(type(arr)) # <class 'numpy.ndarray'>
#ndarray --> n dimensional array

lst1 = [[10,20,30],[40,50,60]] # 2 dimensional array
array = np.array(lst1)
print(type(array)) # <class 'numpy.ndarray'>

## checking the shape of the array
print(array.shape) # (2, 3) --> 2 rows and 3 columns

lst4 = [[[10,20,30],[40,50,60]]]
darray = np.array(lst4)
print(darray.shape) # (1, 2, 3) --> 1 array, 2 rows and 3 columns

#Checking dimension of the array
print(array.ndim) # 2 --> 2 dimensional array
print(darray.ndim) # 3 --> 3 dimensional array
lst5 = [[[[10,20,30]]]]
varray = np.array(lst5)

##########ZEROS##########
# Creating an array of zeros
Zeros = np.zeros((2,3)) # 2 rows and 3 columns
print(Zeros) # [[0. 0. 0.] [0. 0. 0.]]
print(Zeros.size) # 6 --> 2*3 = 6
######### ONES ##########
# Creating an array of ones
Ones = np.ones((2,3)) # 2 rows and 3 columns
print(Ones) # [[1. 1. 1.] [1. 1. 1.]]

#### eye(Kernal filter) ####
# Creating an identity matrix
eye = np.eye(3) # 3 rows and 3 columns
print(eye) # [[1. 0. 0.] [0. 1. 0.] [0. 0. 1.]]

### Aggregrate function ###

# Aggregate function is used to perform operations on the array
# like sum, mean, max, min, median, std, var etc.
lst = [1,2,3,4,5]
arr = np.array(lst)
print(arr.sum()) # 15 --> sum of the array
print(arr.mean()) # 3.0 --> mean of the array
print(arr.max()) # 5 --> max of the array
print(arr.min()) # 1 --> min of the array
print(arr.var()) # 2.0 --> variance of the array
print(arr.std()) # 1.4142135623730951 --> standard deviation of the array

########## Transpose ##########

# Transpose is used to convert rows into columns and columns into rows
lst.Transpose() # 1 dimensional array will not be transposed
Zeros.T # 2 dimensional


## Whenever we are using np.array() then we are creating a new array and not modifying the existing array. Also, this is a float not an integer. This is important to understand when performing operations on the array.

################## Axis ##################
array = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
array3 = array + array2 # Adding two arrays
print(array3) # [[ 6  8] [10 12]]

a = array3.sum(axis=0) # sum of the array along the columns
b = array3.sum(axis=1) # sum of the array along the rows
print(a) # [16 20] --> sum of the array along the columns
print(b) # [14 22] --> sum of the array along the rows
print(array3.sum()) # 36 --> sum of the array

a = np.array([[1,2,3,4,5,6],[10,20,30,40,50,60],[100,200,300,400,500,600],
              [1000,2000,3000,4000,5000,6000]]) # 4 rows and 6 columns

print(a[1:2,:2]) # [[10 20]] --> 1st row and 2nd column
print(a[2:,3:5]) # [[400 500] [600 700]] --> 2nd row and 3rd column
print(a[2:,4:]) # [[500 600] [700 800]] --> 2nd row and 3rd column


