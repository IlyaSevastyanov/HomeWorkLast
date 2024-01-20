
"""
import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()
print(data)

"""
import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
one_hot_encoding = pd.DataFrame()
for category in data['whoAmI'].unique():
    one_hot_encoding[category] = (data['whoAmI'] == category).astype(int)
print(one_hot_encoding)
