import math

radius = float(input("Enter the radius of a circle"))

area = math.pi * radius ** 2
perimeter = 2 * math.pi * radius

print (f"The circle with the radius {radius} has a perimeter of {perimeter:.2f} and an area of {area:.2f}")