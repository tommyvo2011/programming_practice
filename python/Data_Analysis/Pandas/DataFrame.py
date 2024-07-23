import numpy as np
import pandas as pd

from pandas import Series,DataFrame

# Collection of Arrays but with Columns and Names
print("Array with columns and names: ")
data = {"States": ("Florida", "Georgia", "Alabama", "Arkansas"),
        "Capital": ("Tahallasee", "Atlanta", "Montegomery", "Little Rock"),
        "Population": (2.5, 2, 1, 0.5)}

frame = pd.DataFrame(data)

print(frame)

# frame.head() Prints the first two rows of data 
print("Printing with just first two rows of data: ")
print(frame.head(2))

# frame.tail() Prints the last two rows of data
print("Printing with the last two rows of data: ")
print(frame.tail(2))

# The columns can be arranged to your desire
print("Printing with columns arranged: ")
frame1 = pd.DataFrame(data, columns=["Capital", "States", "Population"])
print(frame1)

# A frame can be viewed similar to an array
print(frame1["States"])

# iloc & loc are used to view based on the rows
print(frame.loc[[1,2]])

# Adding a column
print("Adding a frame")
frame["T/F"] = frame["Population"] > 1.5
print(frame)

# Deleting a column
print("Deleting a frame")
del frame["T/F"]
print(frame)

# A DataFrame can also be transposed similar to Numpy arrays
print(frame.T)

# If a DataFrame has a column and a index, you can set its name
frame.index.name = "Series"
frame.columns.name= "Info"
print(frame)
# However one can name a DataFrame, only in an series
'''
Type 	                                            Notes
2D ndarray 	                                        A matrix of data, passing optional row and column labels
Dictionary of arrays, lists, or tuples 	            Each sequence becomes a column in the DataFrame; all sequences must be the same length
NumPy structured/record array 	                    Treated as the “dictionary of arrays” case
Dictionary of Series 	                            Each value becomes a column; indexes from each Series are unioned together to form the result’s row index if no explicit index is passed
Dictionary of dictionaries 	                        Each inner dictionary becomes a column; keys are unioned to form the row index as in the “dictionary of Series” case
List of dictionaries or Series                     	Each item becomes a row in the DataFrame; unions of dictionary keys or Series indexes become the DataFrame’s column labels
List of lists or tuples 	                        Treated as the “2D ndarray” case
Another DataFrame 	                                The DataFrame’s indexes are used unless different ones are passed
NumPy MaskedArray 	                                Like the “2D ndarray” case except masked values are missing in the DataFrame result
'''

#To.numpy() returns the DataFrame without the columns and indexes into a ndarray
print(frame.to_numpy())