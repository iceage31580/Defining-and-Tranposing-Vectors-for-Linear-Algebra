import numpy as np

# create complex number 
z = complex(3,4)
print(f"A complex number {z} in python ")

# magnitude of this complex number 
print("--------- magnitude of a complex number")
print(f"       1. Using 'norm of {z}': {np.linalg.norm(z)} ")
print(f"       2. Using 'transpose(z) * z': {np.transpose(z) * z}.")

#complex vector 
v = np.array([3,4j, 5 + 2j, complex(2, -5), z])
print(f"\n\n Vector with complex elements: {v}")

print(f"->Tranpose of v does not change the imaginary component \n")
print(f"         1. Use 'v.T':               {v.T}"                )
print(f"         2. Use 'tranpose(v)': {np.transpose(v)}          ")
print(f"-> Conjugation changes the sign of the imaginary component")
print(f"   vector with complex numbers: {v}                       ")
print(f"   conjugation using 'v.conjugate()' : {v.conjugate()}    ")
print(f"tranpose of conjugation 'tranpose'(v.conjugate)()': {np.transpose(v.conjugate())}")
