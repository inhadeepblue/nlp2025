import pandas as pd

df1 = pd.read_csv('bike_rentals.csv')
# print(df1.info())
# print(df1.describe())
# print(df1.describe(include='object'))

df2 = pd.read_csv('Bookings.csv')
print(df2.info())
print(df2.describe())
print(df2.describe(include='object'))