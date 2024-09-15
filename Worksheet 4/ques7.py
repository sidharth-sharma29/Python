'''Ques on 7: Reshaping  
7.1 Create a 1D array with 12 elements starting from 11. 
7.2 Reshape it into a 2D array of shape (3, 4). Print the reshaped array. '''

import numpy as np

#7.1
arr=np.arange(11,11+12)
print(f"arr: {arr}")
#7.2
arr1=arr.reshape(3,4)
print(f"After reshaping arr: \n{arr1}")