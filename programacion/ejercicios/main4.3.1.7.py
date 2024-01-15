def is_year_leap(year):
    return year%400==0 or year%4==0 and year%100!=0

def days_in_month(year, month):
    list_months=[31,28,31,30,31,30,31,31,30,31,30,30]
    
    if month == 2 and is_year_leap(year):
        return 29
    else:
        return list_months[month-1]

    return
    

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
