'''Ques on 3: Array Operations  
3.1 Create two 1D arrays: 
 Array1: [2, 4, 6, 8, 10] 
 Array2: [1, 3, 5, 7, 9] 
3.2 Perform the following operations and print the results: 
 Addition 
 Subtraction 
 Element-wise multiplication 
 Element-wise division '''
#3.1
import numpy as np
arr1=np.array([2, 4, 6, 8, 10])
arr2=np.array([1, 3, 5, 7, 9])
print(f"arr1: {arr1}")
print(f"arr2: {arr2}")

#3.2
print(f"arr1 + arr2 = {arr1+arr2}")
print(f"arr1 - arr2 = {arr1-arr2}")
print(f"arr1 * arr2 = {arr1*arr2}")
print(f"arr1 / arr2 = {arr1/arr2}")