import pandas as pd

# create a sample dataframe
'''
df = pd.DataFrameataFrame ({'Name':['John', 'Emma'],
                    'Age':[25,30],
                    'Gender':['Male','Female']})

print(df)
'''
filepath = 'C:\\Users\\anush\\OneDrive\\Documents\\sample dataset\\export1.csv'
df1 = pd.read_csv(filepath)
#print(df1.loc[:,"city"])
#print(df1.loc[0:3,"city"])
# print(df1.loc[0:3,["city", "state"]])

# dfduplicate = df1[df1.duplicated()]
# print(dfduplicate)

# filter the records on the basis of a condition

df_dup = df1[df1.duplicated('TFN')]
print(df_dup)

# df_dup_filter = df_dup.query('TFN == 15613')
# print(df_dup_filter)

# Take a dynamic value into the dataframe query
# TFN_val = input("enter TFN: ")
TFN_val = 15613
df_dup_filter = df_dup.query('TFN == @TFN_val')
print(df_dup_filter)

num_of_records = len(df_dup_filter)
print(num_of_records)

