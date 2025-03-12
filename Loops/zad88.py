
mont = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}


def date_to_days(date):
    date = date.split(".")
    days = int(date[0])
    years = abs(1900 - int(date[2])-1)
    special_dates = years//4
    days += years*365 + special_dates
    mnt = int(date[1])
    for m in range(1,mnt+1):
        days += int(mont[m])
    return days
    

def cnt_days(date1,date2):
    a = date_to_days(date1)
    b = date_to_days(date2)
    return abs(a-b)

print(cnt_days("19.05.1964","21.06.1970")+1)
