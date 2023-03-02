# Vector Defined as a List
import numpy as np
w1 = [1,3,5]
w2 = [3,-4,2]

w3 = np.multiply(w1,w2)
print(f"Hadmard Multiplication of two vectors as a list ")
print(f"Vector1 = {w1} and Vector2 = {w2}")
print(f"The Hadmard multiplication of v1 and v2 = {w3}")

# Vector Defined as an Array
import numpy as np
w1 = [1,3,5]
w2 = [3,-4,2]

w3 = np.array(w1) * np.array(w2)
print(f"Hadmard Multiplication of two vectors as a numpy array ")
print(f"Vector1 = {w1} and Vector2 = {w2}")
print(f"The Hadmard multiplication of v1 and v2 = {w3}")
