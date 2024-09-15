'''10.1 Create a 3x3 matrix:
 
     2 1 3
A =  0 5 6
     7 8 9

10.2 Perform the following operations:
 Find the determinant of matrix A.
 Compute the inverse of matrix A.
 Find the eigenvalues and eigenvectors of matrix A.'''

import numpy as np
#10.1
arr=np.array([[2,1,3],[0,5,6],[7,8,9]])
print(f"3x3 matrix:\n{arr}\n")

#10.2
a=np.linalg.det(arr)
b=np.linalg.inv(arr)
eigen_val,eigen_vect=np.linalg.eig(arr)
print(f"Determinant of matrix A: {a}\n")
print(f"Inverse of matrix A: \n{b}\n")
print(f"Eigenvalues of matrix A = {eigen_val} \n\nEigenvectors of matrix A = \n{eigen_vect}")
