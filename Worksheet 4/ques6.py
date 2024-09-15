'''Ques on 6: Boolean Indexing  
6.1 Create a 1D array with random integers between 20 and 40 (10 elements). 
6.2 Use Boolean indexing to find all elements greater than 30. '''

import numpy as np
#6.1
arr=np.random.randint(20,40,10)
print(f"arr: {arr}")
#6.2
arr1=arr>30
print(arr1)
