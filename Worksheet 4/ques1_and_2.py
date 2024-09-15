'''Ques on 1: Array Crea on  
1.1 Create a 1D array of integers from 5 to 25 using NumPy. 
1.2 Create a 2D array with 3 rows and 4 columns filled with random integers between 10 and 50. '''

import numpy as np
#1.1
arr=np.arange(5,26)
print(f"1D array of integers from 5 to 25: {arr}\n")

#1.2
arr1=np.random.randint(10,50,12).reshape(3,4)
print(f"2D array with 3 rows and 4 columns filled with random integers between 10 and 50:\n{arr1}\n")

'''Ques on 2: Array A ributes  
2.1 For the 1D array created in Ques on 1.1, find, and print its: 
 Shape 
 Size 
 Data type 
2.2 For the 2D array created in Ques on 1.2, find, and print its: 
 Shape 
 Size 
 Data type '''
#2.1
print(f"Shape of 1D array: {arr.shape}")
print(f"Size of 1D array: {arr.size}")
print(f"Data type of 1D array: {arr.dtype}")
print(f"Shape of 2D array: {arr1.shape}")
print(f"Size of 2D array: {arr1.size}")
print(f"Data type of 2D array: {arr1.dtype}")