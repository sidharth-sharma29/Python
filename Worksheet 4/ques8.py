'''Ques on 8: Matrix Opera ons  
8.1 Create two 2x2 matrices: 
 Matrix A: [[1, 2], [3, 4]] 
 Matrix B: [[5, 6], [7, 8]] 
8.2 Perform and print the results of the following opera ons: 
 Matrix multiplication 
 Transpose of Matrix A '''

import numpy as np
#8.1
matrix_A=np.array([[1, 2], [3, 4]])
matrix_B=np.array([[5, 6], [7, 8]])
print(f"matrix A : {matrix_A}\nmatrix B : {matrix_B}")
#8.2
a=matrix_A*matrix_B
b=np.transpose(matrix_A)
print(f"matrix multiplication :\n{a}")
print(f"Transpose of Matrix A:\n{b}")