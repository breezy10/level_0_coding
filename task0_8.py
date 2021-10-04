def convert(time_):
    minutes_ = int(time_)
    hours = time_/60
    minutes = time_ % 60
    if time_ >= 60:
        hrs_str = str(hours)
        hrs, mins= hrs_str.split(".")       
        if mins == '0' and hrs =='1':
            print("%s hour"% hrs)
        elif mins == '0' and hrs > '1':
            print("%s hours "% hrs)
        elif hrs == '1' and mins > '1':
            print("%s hour, %s minutes"% (hrs, minutes))
        else:
            print("%s hours, %s minutes"% (hrs, minutes))
    elif time_ < 60:
        if minutes_ == 1:
            print("%s minute"% minutes_)
        else:
            print("%s minutes"% minutes_)
    else:
        print("Invalid time format")
convert(11)

