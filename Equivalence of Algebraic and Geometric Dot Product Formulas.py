import numpy as np

# Create two vectors

v1 = np.array([2,4,-3]) # numpy does not specify if a vector is a row or column vector
v2 = np.array([0,-3,-3])

# Compute the angle(Radian) between v1 and v2 using arccos
ang = np.arccis((np.dot(v1,v2))/(np.lingalg.norm(v1) * np.linalg.norm(v2))) # don't forget the () in the denominator

# Print(f"The angle between {v1} and {v2} is {ang .1f} in radians and {ang.np.pi * 180.2f} in degrees.")

# Equivalance of algebriac and Geometric Dot Prodict Formulas 

# Create Two Vectors 

v1 = np.array([2,4,-3]) # numpy does not specify if a vector is a row or column vector 
v2 = np.array([0,-3,3])

# Dot Product Algebraic Way

dp_a = np.dot(v1,v2)

# Compute the angle(radian) between v1 and v2 using arccos 

ang = np.arccos(np.dot(v1,v2))/(np.linalg.norm(v1)*np.linalg.norm(v2))) # don't forget the () in the denominator 

# Dot product using Geometry 
dp_g = np.linalg.norm(v1) * np.linalg.norm(v2) * np.cos(ang)

# Print angle in Radians and Degrees

Print(f"The angle between {v1} and {v2} is {ang: .1f} in radians and {ang/np.pi * 180: 2f} in degrees.")

# Print Dot Product using Algebraic and Geometric Formulas 

Print(f"Dot Product using algebriac formula: {dp_a}\n Dot Product using geometric formula: {dp_g}") 
