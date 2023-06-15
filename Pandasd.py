import pandas as pd

technologies = [ ["java",20000, "30days"], 
                 ["python",20000, "40days"], 
               ]
df=pd.DataFrame(technologies)
print(df)
column_names=["Courses","Fee","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)

print(df.dtypes)


technologies = {
    'Courses':["java","python",".net"],
    'Fee' :[20000,25000,26000],
    'Duration':['30day','40days','35days'],
    'Discount':[1000,2300,1500]
              }
df = pd.DataFrame(technologies)
print(df)


df = pd.read_csv('t20.csv')
print(df)


print("**************************")
print(df.shape)

print("**************************")
print(df.size)
print("**************************")
print(df.empty)
print("**************************")
print(df.columns)
print("**************************")
print(df.columns.values)
print("**************************")
print(df.index)
print("**************************")
print(df.index.values)
print("**************************")
print(df.dtypes)
print(df.index.values)
print("**************************")
print(df['Player'])
print(df[['Player','Runs']])
print(df.index.values)
print("**************************")
df2=df[df['Runs'] == 2633]
print(df2)
print("**************************")
df2=df[6:]
print(df2)
print("**************************")
print(df['Runs'][3])
print(df["Runs"].values[3])
print("**************************")
df["dob"] = "10/1/11"
print(df)
print("**************************")
print(df.describe())

