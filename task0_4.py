def even_or_odd():
    number = int(input("Enter a number: "))
    remainder = number % 2
    if (remainder == 0):
        print("even")
    else:
        print("odd")
even_or_odd()