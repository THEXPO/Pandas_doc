import pandas as pd

# Series and DataFrame in pandas

obj = pd.Series([3, 4, 6, 7])
obj

#Series with indexes

obj2 = pd.Series([1, 2, 3, 4, 5], index =["a", "b", "c", "d", "e"])
obj2 

#Series using Dictionary

sdata = {"ohio":35000,"Texas": 71000,"Oregon": 25500,"Utah":44000}
obj3 = pd.Series(sdata)
obj3


#DataFrame in pandas

data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
"year": [2000, 2001, 2002, 2001, 2002, 2003],
"pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

df = pd.DataFrame(data)
df

