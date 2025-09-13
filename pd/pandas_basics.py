import pandas as pd
import seaborn as sns

df = sns.load_dataset('mpg')
print(df)
df = df.drop(columns=['name', 'cylinders'])
# df_asc = df.sort_values('mpg')
# print(df_asc)
df_desc = df.sort_values('mpg', ascending=False)
print(df_desc)