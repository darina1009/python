import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

one_hot_data = pd.crosstab(index=data.index, columns=data['whoAmI'], dropna=False)

print(one_hot_data)
