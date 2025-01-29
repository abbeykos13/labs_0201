import math

a_str = input("Enter the first side of the triangle: ")
b_str = input("Enter the second side of the triangle: ")

a = float(a_str)
b = float(b_str)

c = math.sqrt(a**2 + b**2)

print(f"The hypotenuse is {c:.2f}")