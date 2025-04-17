import random
from datetime import datetime

def generator():
    now_year = datetime.now().year
    year = random.randint(now_year - 5, now_year)
    month = random.randint(1, 12)
    
    if month == 2:
        day = min(28, random.randint(1, 31))
    elif month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    else:
        day = random.randint(1, 31)
    
    return datetime(year, month, day).date()

def raznitsa(date1, date2):
    return abs((date2 - date1).days)

dates = [generator() for y in range(11)]

for i in range(len(dates) - 1):
    print(f"Между {dates[i]} и {dates[i + 1]} -> {raznitsa(dates[i], dates[i + 1])} дней")