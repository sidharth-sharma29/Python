'''4.1 Create a 2D array of shape (3, 3) with values startng from 1 to 9. 
4.2 Using broadcasting, multiply this 2D array by a scalar value of 5. Print the result.'''

import numpy as np
#4.1
arr=np.arange(1,10).reshape(3,3)
print(f'arr = \n{arr}')

#4.2
print("arr * 5 =")
b=arr*5
print(b)