import pandas as pd
import seaborn as sns

# print(sns.get_dataset_names())
titanic = sns.load_dataset('titanic')
print(titanic)
print(titanic[['sibsp', 'parch', 'fare']])

print(titanic[titanic.age > 70])
print(titanic.sample(n=7))
print(titanic.nlargest(4, 'age'))