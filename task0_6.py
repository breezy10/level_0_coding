def maximum():
    a = float(12)
    b = float(9)
    c = float(92)
    print("Maximum is ", end = '')
    if b <= a >= c:
        print(a)
    elif a <= b >= c:
        print(b)
    elif a <= c >= b:
        print(c)
maximum()