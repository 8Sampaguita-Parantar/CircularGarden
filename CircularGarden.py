#Author - Aldrich John P. Parantar
#Date - 9/19/2026
#Purpose - To calculate the area, circumference, area square root, and area rounded to either up or down with its radius.

#INPUT - Asks the user to enter the circle's radius.
import math
radius = float(input("Enter the circle's radius: "))

#PROCESSING - Processes the given radius to calculate all of the given dimensions.
area = math.pi * math.pow(radius, 2)
circumference = 2 * math.pi * radius
area_squareroot = math.sqrt(area)
area_rounddown = math.floor(area)
area_roundup = math.ceil(area)

#OUTPUT - Displays all the dimensions calculated in processing.
print(f"Area of the garden: {area:.2f} square meters")
print(f"Circumference of the garden: {circumference:.2f} meters")
print(f"Square root of the area: {area_squareroot:.2f}")
print(f"Area rounded down: {area_rounddown} square meters")
print(f"Area rounded up: {area_roundup} square meters")