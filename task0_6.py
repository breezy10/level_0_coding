def maximum():
    a = float(input("Enter 1st number: "))
    b = float(input("Enter 2nd number: "))
    c = float(input("Enter 3rd number: "))
    print("Maximum is ", end = '')
    if b <= a >= c:
        print(a)
    elif a <= b >= c:
        print(b)
    elif a <= c >= b:
        print(c)
maximum()