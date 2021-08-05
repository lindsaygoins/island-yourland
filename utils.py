def convert_date(num):
    if num == 0:
        month = "Jan"
    elif num == 1:
        month = "Feb"
    elif num == 2:
        month = "Mar"
    elif num == 3:
        month = "Apr"
    elif num == 4:
        month = "May"
    elif num == 5:
        month = "Jun"
    elif num == 6:
        month = "Jul"
    elif num == 7:
        month = "Aug"
    elif num == 8:
        month = "Sep"
    elif num == 9:
        month = "Oct"
    elif num == 10:
        month = "Nov"
    elif num == 11:
        month = "Dec"
    return month

def convert_time(num):
    if num == 0:
        num += 12
        time = str(num) + " AM"
    elif num < 13:
        time = str(num) + " AM"
    else:
        num -= 12
        time = str(num) + " PM"
    return time