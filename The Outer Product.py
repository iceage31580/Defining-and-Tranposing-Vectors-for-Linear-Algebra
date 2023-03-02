import numpy as np

# v and w vectors
v = np.array([1, 2, 3])
w = np.array([-1, 0, 3, -2])
# initialize a zero matrix with row and column

op_vw = np.zeros((len(v), len(w))) # zeros((row, col)) The inside paranthesis is for setting dimentions

# Loop through element of the first vector
for i in range(0, len(v)): # default range(len(v)), it is exclusive on the right ending, does not include the last element of range
    #indentation for the i loop
    for j in range(len(w)):
        #indentation for the j loop
        op_vw[i, j] = v[i] * w[j]

print(f"The outer product of vevtor {v} and vector {w}\nusing native python = vw^T =\n{op_vw}")
