import random
import math

# Generate two random integer vectors in R4
v1 = [random.randint(-10, 10) for i in range(4)]
v2 = [random.randint(-10, 10) for i in range(4)]

# Compute the length of each vector
len_v1 = math.sqrt(sum([x**2 for x in v1]))
len_v2 = math.sqrt(sum([x**2 for x in v2]))

# Compute the magnitude of the dot product
dot_product = sum([a * b for a, b in zip(v1, v2)])
mag_dot_product = abs(dot_product)

# Normalize the two vectors to unit vectors
unit_v1 = [x/len_v1 for x in v1]
unit_v2 = [x/len_v2 for x in v2]

# Compute the magnitude of the dot product of the normalized vectors
dot_product_norm = sum([a * b for a, b in zip(unit_v1, unit_v2)])
mag_dot_product_norm = abs(dot_product_norm)

# Print the results
print("Generated vectors:")
print("v1:", v1)
print("v2:", v2)
print()
print("Length of vectors:")
print("Length of v1:", len_v1)
print("Length of v2:", len_v2)
print()
print("Magnitude of dot product:")
print("Magnitude of dot product:", mag_dot_product)
print()
print("Unit vectors:")
print("Unit vector of v1:", unit_v1)
print("Unit vector of v2:", unit_v2)
print()
print("Magnitude of dot product of normalized vectors:")
print("Magnitude of dot product of normalized vectors:", mag_dot_product_norm)
