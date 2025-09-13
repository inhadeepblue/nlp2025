import pandas as pd

df1 = pd.DataFrame({
    #'date' : ['2025-09-13', '2025-09-13', '2025-09-14', '2025-09-15'],
    'date' : ['2025-09-13', '2025-09-13', '2025-09-14', '2025-09-14'],
    'city' : ['Seoul', 'Incheon', 'Seoul', 'Incheon'],
    'temp' : [25, 24, 27, 24]
})
print(df1)
df2 = df1.pivot(index='date', columns='city', values='temp')
print()
print(df2)