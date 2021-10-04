# Python Program to find Area of a Triangle using Functions
import math

def Area_of_triangle(a, b, c):
# calculate the semi-perimeter
    s = (a + b + c) / 2

# calculate the area
    area = math.sqrt((s*(s-a)*(s-b)*(s-c)))

    print(area)

#input of a sides    
a = float(input('enter a: '))
b = float(input('enter b: '))
c = float(input('enter c: '))

Area_of_triangle(a,b,c)