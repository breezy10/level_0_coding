def timeconverter():
    time = float(17)
    hour = time // 60
    time %= 60
    minute = time
    print(hour, "hours", minute, "minutes")
timeconverter()