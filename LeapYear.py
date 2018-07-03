def solve(year):
    date = ""
    if (year <= 1917 and year >= 1700) or (year >= 1919 and year <= 2700):
        if isLeap(year):
            date = "12.09." + str(year)
        else:
            date = "13.09." + str(year)
    elif year == 1918:
        days = 256 - 33 - 14 
        month = 0
        for i in range(3,10):
            if days >= 30:
                if i%2 == 0:
                    days -= 31
                else:
                    days -= 30
            else:
                month = i
                break
        if days/10 == 0:
            date = "0"+str(days)+".0"+str(month)+".1918"
        else:
            date = str(days)+".0"+str(month)+".1918"
    
    return date

print solve(1918)