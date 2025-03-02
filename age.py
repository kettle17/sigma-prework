from datetime import date
from datetime import datetime
curr_date = date.today()


def diff_dates(date1, date2):
    return abs(date2-date1).days


def calc_age(given_date):
    # convert string to date
    try:
        given_date = datetime.strptime(given_date, '%d-%m-%Y').date()
    except:
        raise Exception("Incorrect input")
    # get difference between today + given date
    new_date = diff_dates(given_date, curr_date)
    # as of today 01-01-1990 would return 35
    # desyncs with leapyears
    return round(new_date / 365)


print(calc_age(input("Please input a date in the format D-M-Y")))
