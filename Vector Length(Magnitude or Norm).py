import numpy as np

# Define the vector
v = [6, 5, 0.2, 321, 0.1, 3.2, 8]

# Method 1: Dot product using a for loop
dotProduct1 = 0
for i in range(len(v)-1):
    dotProduct1 += v[i] * v[i+1]

# Method 2: Dot product using numpy dot function
v1 = np.array(v)
dotProduct2 = np.dot(v1[:-1], v1[1:])

# Method 3: Dot product using numpy tensordot function
dotProduct3 = np.tensordot(v1[:-1], v1[1:], axes=1)

# Method 4: Dot product using list comprehension
dotProduct4 = sum([v[i] * v[i+1] for i in range(len(v)-1)])

# Method 5: Dot product using numpy inner function
dotProduct5 = np.inner(v1[:-1], v1[1:])

# Calculate the square root of the result for each method
v_len_1 = np.sqrt(dotProduct1)
v_len_2 = np.sqrt(dotProduct2)
v_len_3 = np.sqrt(dotProduct3)
v_len_4 = np.sqrt(dotProduct4)
v_len_5 = np.sqrt(dotProduct5)

# Save the norm for each method in v_len_1 ... to v_len_5
print(f"Using math formula for dot product of vector {v}")
print(f"The length, magnitude, or norm of the vector v is:\n{v_len_1:.2f},\n{v_len_2:.2f},\n{v_len_3:.2f},\n{v_len_4:.2f},\n{v_len_5:.2f}")

# Calculate the norm using numpy.linalg
v_len_6 = np.linalg.norm(v)
print(f"Using numpy.linalg, we can calculate norm directly: {v_len_6:.2f}")

# Calculate the length of vector using numpy
v1 = np.array([2, 3])
length = np.sqrt(np.sum(np.square(v1))) 
print(f"Length of vector {v1} using numpy: {length:.2f}")
