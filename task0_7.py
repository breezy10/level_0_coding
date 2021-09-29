def fahrenheit():
    celsius = float(input("Enter temperature in Degrees Celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print(fahrenheit, "Degrees Fahreinheit." )
fahrenheit()

def celsius():
    fahrenheit = float(input("Enter teperature in Degrees Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(celsius, "Degrees Celsius.")
celsius()

