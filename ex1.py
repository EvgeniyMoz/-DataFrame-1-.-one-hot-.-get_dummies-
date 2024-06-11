import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем пустой DataFrame с колонками, соответствующими уникальным значениям столбца 'whoAmI'
one_hot_data = pd.DataFrame(columns=data['whoAmI'].unique())

# Заполняем one-hot DataFrame значениями 0
one_hot_data = one_hot_data.fillna(0)

# Заменяем значения в one-hot DataFrame на 1, где соответствующее значение в столбце 'whoAmI' равно 1
for i, value in enumerate(data['whoAmI']):
    one_hot_data.loc[i, value] = 1

# Объединяем исходный DataFrame и one-hot DataFrame
data = pd.concat([data, one_hot_data], axis=1)

data.head()
