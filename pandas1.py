import pandas as pd
df = pd.read_csv('IPL_Matches_2008_2022.csv')
#print(df)
print(df.loc[1:5].loc[:,["City","Team1"]])
print(df.loc[1:5].loc[:,"City":"Team1"])
print(df.loc[1:5].loc[:,"City":])
print(df.loc[1:5].loc[:,:"Season"])
print(df.loc[df["City"]=="Ahmedabad"])

print("******************")
print(df.iloc[1:8])
print(df.iloc[1:8:,-4:-1])
print("************************")


print(df.where(df.City=="Ahmedabad","NA",))

print("************************")

print(df.filter(items=["City","Umpire1"]))
print(df.filter(items=[1,4],axis=0))
print(df.filter(like='23',axis=0))
print("************************")
print(df.query("City in ('Delhi','Hyderabad')"))
print(df.query(" `Umpire1 City` != 'Delhi'"))

import pandas as pd
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Hadoop","Spark","Python","NA"],
    'Fee' :[22000,25000,23000,24000,26000,25000,25000,22000,1500],
    'Duration':['30days','50days','55days','40days','60days','35days','30days','50days','40days'],
    'Discount':[1000,2300,1000,1200,2500,None,1400,1600,0]
          })
df = pd.DataFrame(technologies)
print(df)

# Use groupby() to compute the sum
df2 =df.groupby(['Courses']).sum()
print(df2)

# Group by on multiple columns
df2 =df.groupby(['Courses', 'Duration']).sum()
print(df2)

# Set Index on group by results
df2 = df.groupby(['Courses','Duration']).sum().reset_index()
print(df2)

# Using groupby on single column in pandas 
df2 = df.groupby(['Courses'])['Fee'].sum().reset_index()
print(df2)

# Ignore sorting on group by key
df2=df.groupby(by=['Courses'], sort=False).sum()
print(df2)

# Sort group key on descending order
groupedDF = df.groupby('Courses',sort=False).sum()
sortedDF=groupedDF.sort_values('Courses', ascending=False)
print(sortedDF)

# Groupby & multiple aggregations
result = df.groupby('Courses')['Fee'].aggregate(['min','max'])
print(result)

# Groupby multiple columns & multiple aggregations
result = df.groupby('Courses').aggregate({'Duration':'count','Fee':['min','max']})
print(result)