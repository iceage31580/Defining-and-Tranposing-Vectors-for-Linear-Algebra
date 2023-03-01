import numpy as np

# define variables for dimensions
n = 5
m = 5
k = 5

# create three random vectors a, b, and c
a = np.random.randn(n)
b = np.random.randn(m)
c = np.random.randn(k)

# calculate the left and right side of the associative property 
left = np.dot(a, np.dot(b,c))
right = np.dot(np.dot(a,b),c)

# compare the answers and output the results
print(f"vector a = {a}")
print(f"vector b = {b}")
print(f"vector c = {c}")
print(f"\n left and right sides of the associative property formula = \n {left} \n {right}")
print(f"\n difference between the left and right side of the associative property\n{left- right}")

# test the associative property with random vectors and count the number of times left and right are equal
count_false = 0
for i in range(10): 
    a = np.random.randn(n)
    b = np.random.randn(m)
    c = np.random.randn(k)
    left = np.dot(a, np.dot(b,c))
    right = np.dot(np.dot(a,b),c)
    if np.array_equal(left,right):
      count_false += 1
print(f"The number of times left and right are equal in the associative property is {count_false}")

# test the associative property with smaller dimensions and count the number of times left and right are equal
n = 5
m = 3
k = 3
count_false = 0
for i in range(10): 
    a = np.random.randn(n)
    b = np.random.randn(m)
    c = np.random.randn(k)
    left = np.dot(a, np.dot(b,c))
    right = np.dot(np.dot(a,b),c)
    if np.array_equal(left,right):
      count_false += 1
print(f"The number of times left and right are equal in the associative property is {count_false}")

# test the associative property with one dimension equal to zero and count the number of times left and right are equal
n = 0
m = 5
k = 5
count_false = 0
for i in range(10): 
    a = np.random.randn(n)
    b = np.random.randn(m)
    c = np.random.randn(k)
    left = np.dot(a, np.dot(b,c))
    right = np.dot(np.dot(a,b),c)
    if np.array_equal(left,right):
      count_false += 1
print(f"The number of times left and right are equal in the associative property is {count_false}")

# test the associative property with two vectors equal to each other and count the number of times left and right are equal
n = 5
m = 5
k = 5
count_false = 0
for i in range(10): 
    b = np.random.randn(m)
    a = c = b
    left = np.dot(a, np.dot(b,c))
    right = np.dot(np.dot(a,b),c)
    if np.array_equal(left,right):
      count_false += 1
print(f"The number of times left and right are equal in the associative property is {count_false}")
