import numpy as np
import matplotlib as plt

arr = np.random.standard_normal(5)

arr1 = np.array(['Will','Tom', 'Jordan', 'Patrick', 'Jenny'])

print(arr)

print(arr > 0.5)

arr_subbed = np.where(arr < 0, 2, arr)

print(arr_subbed)

sorted_arr = np.sort(arr_subbed)

print(sorted_arr)


