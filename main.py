# Shape & Reshaping in Numpy Arrays
import numpy as np
var = np.array([[1,2],[3,4]])
print(var)
print(var.shape)

#multidimensional array
var1 = np.array([1,2,3,4],ndmin=4)
print(var1)
print(var1.ndim)
print(var1.shape)

#RESHAPE
var2 = np.array([1,2,3,4,5,6])
print(var2)
print(var2.ndim)


x = var2.reshape(3,2)
print(x)
print(x.ndim)

#  3 denote  number of row
# 2 denote how many element we want to pass in each row
# elements must be equal divide in rows or it will give error
 #array can not produce empty array


# 3 dimensional array
var3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(var3)
print(var3.ndim)
print()
x1 = var3.reshape(2,3,2)
print(x1)



test1 = np.array([1,2,3,4,5,6,7,8])
print(type(test1))
print( test1.ndim)
test1 = np.array([1,2,3,4],ndmin=2)
print(test1)
print(test1.reshape(2,2))
print(test1 .ndim)

x3 = test1.reshape(2,2)
print(x3)
print(x3.ndim)
print(x3.shape)