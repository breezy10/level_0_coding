def timeconverter():
    time = float(input("Enter a number:"))
    hour = time // 60
    time %= 60
    minute = time
    print(hour, "hours", minute, "minutes")
timeconverter()