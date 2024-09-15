'''Ques on 5: Slicing and Indexing  
5.1 Create a 2D array of shape (4, 4) with values ranging from 10 to 25. 
5.2 Extract the second row and the last column of the array. 
5.3 Replace the elements of the first row with zeros. '''

import numpy as np
#5.1
arr=np.arange(10,26).reshape(4,4)
print(f"arr:\n{arr}")
#5.2
print(f"The second row:{arr[1]}\nThe last column of the array: {arr[:,3]}")
#5.3
arr[0,:]=0
print(f"After replacing the elements of the first row with zeros:\n{arr}")