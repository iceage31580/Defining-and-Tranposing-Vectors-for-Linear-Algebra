import numpy as np

# Define the first vector
a = np.array([1, 2, 3])

# Define the second vector
b = np.array([4, 5, 6])

# Define the third vector, which is linearly dependent on the first vector
c = 2 * a

# Compute the dot product of the first and second vectors
dot_ab = np.dot(a, b)

# Compute the dot product of the first and third vectors
dot_ac = np.dot(a, c)

# Compute the dot product of the second and third vectors
dot_bc = np.dot(b, c)

# Compute the norms of the vectors
norm_a = np.linalg.norm(a)
norm_b = np.linalg.norm(b)
norm_c = np.linalg.norm(c)

# Compute the products of the norms
norm_a_norm_b = norm_a * norm_b
norm_a_norm_c = norm_a * norm_c
norm_b_norm_c = norm_b * norm_c

# Print the results for the left and right side of the Cauchy-Schwarz inequality
print("Left side of the Cauchy-Schwarz inequality:", dot_ab)
print("Right side of the Cauchy-Schwarz inequality:", norm_a_norm_b)
print("Left side of the Cauchy-Schwarz inequality:", dot_ac)
print("Right side of the Cauchy-Schwarz inequality:", norm_a_norm_c)
print("Left side of the Cauchy-Schwarz inequality:", dot_bc)
print("Right side of the Cauchy-Schwarz inequality:", norm_b_norm_c)
