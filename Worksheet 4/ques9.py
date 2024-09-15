'''Ques on 9: Sta s cal Func ons  
9.1 Create a 1D array with random integers between 10 and 60 (15 elements). 
9.2 Compute and print the following statistics: 
 Mean 
 Median 
 Standard deviation'''

import numpy as np
#9.1
a=np.random.randint(10,60,15)
print(a)
#9.2
x=np.median(a)
y=np.mean(a)
z=np.std(a)
print(f"Median: {x}\nMean: {y}\nStandard deviation: {z}")
