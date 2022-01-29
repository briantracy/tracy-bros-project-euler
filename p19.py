



def thirty_day_month(year):
    return 30
def thirty_one_day_month(year):
    return 31
def february(year):
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        return 29
    else:
        return 28

days_per_month = {
    0: thirty_one_day_month, # Jan
    1: february, # Feb
    2: thirty_one_day_month, # Mar
    3: thirty_day_month, # Apr
    4: thirty_one_day_month, # May
    5: thirty_day_month, # Jun
    6: thirty_one_day_month, # Jul
    7: thirty_one_day_month, # Aug
    8: thirty_day_month, # Sep
    9: thirty_one_day_month, # Oct
    10: thirty_day_month, # Nov
    11: thirty_one_day_month, # Dec
}

# Running this starting from day_of_week = 0 and year = 1900,
# we find that the first day of 1901 was a Tuesday. Start here
# and run until 2000

day_of_week = 1 # Tuesday
sundays = 0

for year in range(1901, 2001):
    for month in range(12):
        if day_of_week == 6:
            sundays += 1
        day_of_week += days_per_month[month](year)
        day_of_week %= 7

print(sundays)
