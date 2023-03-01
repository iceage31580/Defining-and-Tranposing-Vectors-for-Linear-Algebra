import numpy as np

# set the number of rows and columns
row_num = 4
col_num = 6

# create a zero vector with the length of the number of columns
vector = np.zeros(col_num)

# create two random matrices of specified dimensions
matrix1 = np.random.randn(row_num, col_num)
matrix2 = np.random.randn(col_num, row_num)

# create a zero matrix with the dimensions of the two input matrices
result = np.zeros((row_num, row_num))

# compute the dot product of the ith column of matrix1 and ith row of matrix2
# and store it in the ith element of the vector
for i in range(col_num):
    vector[i] = np.dot(matrix1[:, i], matrix2[i, :])

# print the resulting vector
print(vector)
