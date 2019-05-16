import pandas as pd

values =[[1,2,3],[4,5,6],[7,8,9]]
index = ['one','two','three']
columns = ['a','b','c']

df = pd.DataFrame(values,index=index,columns=columns)

print(df)
print(df.values)
print(df.index)
print(df.columns)


data = [
    ['1000', 'Steve', 90.72], 
    ['1001', 'James', 78.09], 
    ['1002', 'Doyeon', 98.43], 
    ['1003', 'Jane', 64.19], 
    ['1004', 'Pilwoong', 81.30],
    ['1005', 'Tony', 99.14],
]
df = pd.DataFrame(data)
print(df)


data = {
	'A' : [1,2,3],
	'B' : [4,5,6],
	'C' : [7,8,9]
}
df = pd.DataFrame(data)
print(df)
print(df.head(1))
print(df.tail(1))
print(df['A'])



