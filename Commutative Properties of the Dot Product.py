import numpy as np

# Generate two 2-element random vectors
a = np.random.randint(1, 10, 2)
b = np.random.randint(1, 10, 2)

# Print the vectors
print(a)
print(b)
print()

# Compute a^T * b and b^T * a, and test for equality
dp_ab = 0
dp_ba = 0
for i in range(2):
    dp_ab += a[i] * b[i] 
    dp_ba += b[i] * a[i]
print(dp_ab, dp_ba, dp_ab - dp_ba)
print()

# Step 4 - 5
nu_zero = 0
for j in range(10):
    a = np.random.randint(1, 10, 2)
    b = np.random.randint(1, 10, 2)
    print(a)
    print(b)
    print()

    # Compute a^T * b and b^T * a, and test for equality
    dp_ab = 0
    dp_ba = 0
    for i in range(2):
        dp_ab += a[i] * b[i] 
        dp_ba += b[i] * a[i]
    dif_dp = dp_ab - dp_ba
    print(dp_ab, dp_ba, dif_dp)
    print()

    if dif_dp != 0:
        print(dif_dp)
        nu_zero += 1
print(f"Number of nonzero differences is {nu_zero}.")

# Generate two 1000 element vectors
a = np.random.rand(1000)
b = np.random.rand(1000)

# Compute a^T * b and b^T * a, and test for equality
dp_ab = np.dot(a, b)
dp_ba = np.dot(b, a)
print(dp_ab, dp_ba, dp_ab - dp_ba)
print()

# Test with 2-element random vectors
v = [2, 4]
w = [3, 5]
print(np.dot(v, w), np.dot(w,v), np.dot(v, w) - np.dot(w,v))

# Test with 1000 element random vectors
nu_zero = 0
for i in range(10000):
    a = np.random.rand(1000)
    b = np.random.rand(1000)

    # Compute a^T * b and b^T * a, and test for equality
    dp_ab = np.dot(a, b)
    dp_ba = np.dot(b, a)
    dif_dp = dp_ab - dp_ba
    if dif_dp != 0:
        print(dif_dp)
        nu_zero += 1
print(f"Number of nonzero differences is {nu_zero}.")
