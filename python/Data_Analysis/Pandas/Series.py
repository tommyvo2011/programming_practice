import numpy as np
import pandas as pd

from pandas import Series, DataFrame

obj = pd.Series([0,3,6,69], index = ["A","B","C","D"])
print(obj)
print(obj.array)
print(obj.index)


# Can a dictionary into a pandas array
states = {1 : "Florida", "A": "Alabama", 3: "Georgia", 4: "California"}
obj2= pd.Series(states)
print(obj2)

# Can revert a pandas array back into a dictionary
data = obj2.to_dict()
print(data)

# Can change the name of your Series, Index, & Column
obj.name ="Series of Random Numbers"
obj.index.name= "Index Title"
print(obj)

# Can change the index of the array by hard code assigning
obj.index = [1, 2, 3, 4]
print(obj)
