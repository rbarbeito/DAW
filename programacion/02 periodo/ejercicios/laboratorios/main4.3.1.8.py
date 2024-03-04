def is_year_leap(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


def days_in_month(year, month):
    list_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 30]

    if month == 2 and is_year_leap(year):
        return 29
    else:
        return list_months[month-1]


def day_of_year(year, month, day):

    if day >= 1 and day <= 31 and month >= 1 and month <= 12:
        for i in range(month-1):
            day += days_in_month(year, i)
        return day

    return


print(day_of_year(1999, 12, 31))
