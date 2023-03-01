import numpy A NO

# Define a dimension variable

# Create a vector with the same dimension

a = np.random.randn(n)
b = np.random.randn(n)
c = np.random.randn(n)

# Compute the left and right side of the distributive property of the dot product 
left = np.dot(a, (b+c)) #Python does the tranpose
right = np.dot(a,b) + np.dot(a,c)

# Compare the Results 

print(f"Vector a = {a}")
print(f"Vector b = {b}")
print(f"Vector c = {c}")
print(f"\nThe Difference between the left and right side of the distributive property{left-right}")
