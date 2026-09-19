# Program for Circular Garden

## Author
Name: Aldrich John P. Parantar

Section: 8 - Sampaguita

## Step 1 - Problem Identification
We are looking to find the values of the circle's dimensions.
## Step 2 - Problem Decomposition
All we will have to calculate is the area, circumference, area square root, and the area rounded either down or up.
## Step 3 - Pattern Recognition
The program simply needs math library functions we have used from earlier activities, particularly math.pi to approximate its value.
## Step 4 - Abstraction
We will use math.pi, math.sqrt, math.pow, math.ceil, and math.floor.
## Step 5 - Algorithm
import math

radius = float(input("Enter the circle's radius: "))

area = math.pi * math.pow(radius, 2)

circumference = 2 * math.pi * radius

area_squareroot = math.sqrt(area)

area_rounddown = math.floor(area)

area_roundup = math.ceil(area)

print(f"Area of the garden: {area:.2f} square meters")

print(f"Circumference of the garden: {circumference:.2f} meters")

print(f"Square root of the area: {area_squareroot:.2f}")

print(f"Area rounded down: {area_rounddown} square meters")

print(f"Area rounded up: {area_roundup} square meters")