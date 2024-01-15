def is_year_leap(year): 
    return year%400==0 or year%4==0 and year%100!=0


def days_in_month(year, month):
    list_months=[31,28,31,30,31,30,31,31,30,31,30,30]
    
    if month == 2 and is_year_leap(year):
        return 29
    else:
        return list_months[month-1]

def day_of_year(year, month, day):
#
# Escribe tu código nuevo aquí.
#

print(day_of_year(2000, 12, 31))
