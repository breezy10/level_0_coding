def area_of_triangle():
    a = float(15)
    b = float(11)
    c = float(8)

    p = (a + b + c)
    s = p / 2 
    area = (s*(s-a)*(s-b)*(s-c))** 0.5

    print("The area of the Triangle is:", area)
    print("The Perimeter of the shape is:", p)
    print("The semiperimeter of the triangle is:", s)
area_of_triangle()