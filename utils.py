from copy import deepcopy

def convert_date(num):
    """Convert the integer form of the month to its 3 letter abbreviation."""
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
    """Convert 24-hour time to 12-hour time."""
    if num == 0:
        num += 12
        time = str(num) + " AM"
    elif num < 13:
        time = str(num) + " AM"
    else:
        num -= 12
        time = str(num) + " PM"
    return time

def convert_rows(result):
    """Copy the result from the query and convert the start/end months and hours"""
    # Deep-copy because you can only iterate over the result once
    rows = []
    for row in result:
        rows.append(deepcopy(row[0]))

    for row in rows:

        if row.monthstart == row.monthend:
            row.monthstart = "All Year"
            row.monthend = None
        
        else:
            row.monthstart = convert_date(row.monthstart)
            row.monthend = convert_date(row.monthend)

        if row.altmonthstart:
            row.altmonthstart = convert_date(row.altmonthstart)
            row.altmonthend = convert_date(row.altmonthend)

        if row.hourstart == row.hourend:
            row.hourstart = "All Day"
            row.hourend = None

        else:
            row.hourstart = convert_time(row.hourstart)
            row.hourend = convert_time(row.hourend)

        if row.althourstart:
            row.althourstart = convert_time(row.althourstart)
            row.althourend = convert_time(row.althourend)
            
    return rows