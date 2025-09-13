import numpy as np
import pandas as pd

# df1 = pd.DataFrame(
#     {"id": [100, 102, 107],
#      "math" : [99, 100, 97],
#      "english" : [95, 92, 94]
#      }, index=[1, 2, 3]
# )
# print(df1)
df2 = pd.DataFrame(
    [
        [100, 99, 95],
        [102, 100, 92],
        [107, 97, 94],
    ], columns=["id", "math", "english"], index=[1, 2, 3]
)
print(df2)
# df3 = pd.melt(df2)
# df3 = pd.melt(df2).rename(columns={'variable':'var', 'value':'val'})
df3 = pd.melt(df2).rename(columns={'variable':'var', 'value':'val'}).query('val > 95')
print(df3)