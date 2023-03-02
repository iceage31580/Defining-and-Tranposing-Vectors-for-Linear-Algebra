import numpy as np
import random 

#Generate Two Integers on R^3
vector1 = [random.randint(-10,10) for i in range(3)]
vector2 = [random.randint(-10,10) for i in range(3)]

print("Vector 1:", vector1)
print("Vector 2:", vector2)

#Genereate two scalars and print out the scalars
scalar1 = random.uniform(-10,10)
scalar2 = random.uniform(-10,10)

print("Scalar 1:", scalar1)
print("Scalar 2:", scalar2)

#Compute the dot product between the vectors 

dot_product = sum([a * b for a,b in zip(vector1, vector2)])

print("Dot product:", dot_product)

# Compute the dot product between scaledvectors by two scalars 
scaled_vector1 = [scalar1 * x for x in vector1]
scaled_vector2 = [scalar2 * x for x in vector2]

dot_product2 = sum([a * b for a, b in zip(scaled_vector1, scaled_vector2)])
print("The multiplication of the scalar and the dot product: ", dot_product2)
