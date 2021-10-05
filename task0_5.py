import math

def Area_of_triangle(a, b, c):
# calculate the semi-perimeter
    s = (a + b + c) / 2

# calculate the area
    area = math.sqrt((s*(s-a)*(s-b)*(s-c)))

    print(area)

Area_of_triangle(2,2,2)