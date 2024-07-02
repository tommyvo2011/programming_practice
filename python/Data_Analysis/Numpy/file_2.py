import numpy as np
import pandas as ps
import matplotlib as plt

num_of_dates = int(input("What is the size of this array?"))
arr_dates = np.zeros(num_of_dates)

print(arr_dates)

def random_dates_in_range(num_of_dates, start_date,range_in_days):
    days_add = np.arange(0, range_in_days)
    random_date = np.datetime64(start_date) + np.random.choice(days_add)

    
    print(random_date)

for x in arr_dates:
        arr_dates[x] = random_dates_in_range(num_of_dates,"2024-06-25",30)

print(arr_dates)
#random_date = random_dates_in_range("2015-05-05", 30) 

