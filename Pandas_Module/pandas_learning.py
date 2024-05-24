import pandas as pd
from numpy.random import randint

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# load data into a DataFrame object:
df = pd.Series(data)

print(df)

print()
print(df["calories"])

series1 = pd.Series(data={"a": 12, "b": 23, "c": 45, "d": 85})
series2 = series1+df
print()

print(series2)

print("***********************************************8")
df = pd.DataFrame(data)
print(df)

print(df["calories"][0])
print("***********************************************8")
df = pd.DataFrame(randint(0, 12), [9, 8, 7, 6], ["A", "B", "C"])
print(df)


print("***********************************************8")
print
print(df.loc[9])
print("***********************************************8")
print
print(df[["A", "B"]])
print("***********************************************8")
print
data = {
    "company": ["abc", "abc", "google", "google", "amazon", "clecotech"],
    "sales": [14, 58, 69, 8, 9, 47],
    "person": ["ra", "hel", "fog", "hog", "my", "jar"]
}
df = pd.DataFrame(data)
print(df)
print("***********************************************8")
print()
print("***********************************************8")
print()


arrays = [['A', 'A', 'B', 'B'], [1, 2, 1, 2]]
tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples, names=['First', 'Second'])
print(index)
df=pd.DataFrame(index)
print(df)
data = [[1, 2], [3, 4], [5, 6], [7, 8]]
df = pd.DataFrame(data, index=index, columns=['Value1', 'Value2'])

print(df)