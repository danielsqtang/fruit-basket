import pandas as pd
import sys

file_name = sys.argv[1]
basket = pd.read_csv(file_name)

# data cleanup, whitespace and data in wrong column
char1_values = ('sweet', 'bitter', 'tart', 'heavy')
char2_values = ('red', 'green', 'round', 'prickly', 'yellow')

for i in range(len(basket)):
    char1 = basket['characteristic1'][i].strip()
    char2 = basket['characteristic2'][i].strip()
    if char1 in char2_values and char2 in char1_values:
        basket.loc[i, 'characteristic1'], basket.loc[i, 'characteristic2'] = char2, char1
    else:
        basket.loc[i, 'characteristic1'], basket.loc[i, 'characteristic2'] = char1, char2

# Total Fruit
total_fruit = str(len(basket.index))

# Types of Fruit
types_fruit = str(len(pd.unique(basket['fruit'])))

# Number of types of fruit
num_type_fruit = basket.groupby(['fruit'])['fruit'].count().sort_values(ascending=False)

# Characteristics of fruit group by table
fruit_characteristics_df = basket.groupby(['fruit',
                                           'characteristic1',
                                           'characteristic2'])['fruit'].count().reset_index(name='count')

fruit_characteristics = []
for i in range(len(fruit_characteristics_df)):
    count = str(fruit_characteristics_df['count'][i])
    if int(count) >= 2:
        fruit = str(fruit_characteristics_df['fruit'][i]) + 's'
    else:
        fruit = str(fruit_characteristics_df['fruit'][i])
    characteristic1 = str(fruit_characteristics_df['characteristic1'][i])
    characteristic2 = str(fruit_characteristics_df['characteristic2'][i])
    fruit_characteristics.append(count + ' ' +
                                 fruit + ': ' +
                                 characteristic1 + ', ' +
                                 characteristic2)

# fruit over 3 days old
old_fruit = basket[basket.days > 3].groupby(['fruit'])['fruit'].count().sort_values(ascending=False)
old_fruits = []
for i in range(len(old_fruit)):
    if old_fruit[i] > 1:
        old_fruits.append(str(old_fruit[i]) + ' ' + str(old_fruit.index[i]) + 's')
    else:
        old_fruits.append(str(old_fruit[i]) + ' ' + str(old_fruit.index[i]))
old_fruits_string = ' and '.join(old_fruits)


def print_fruit_statistics():
    print('Total number of fruits: ' + total_fruit)
    print('\n')
    print('Types of fruits: ' + types_fruit)
    print('\n')
    print('The number of each type of fruit in descending order:')
    print(num_type_fruit)
    print('\n')
    print('The characteristics (size, color, shape, etc.) of each fruit by type:')
    print('\n'.join(fruit_characteristics))
    print('\n')
    print('Have any fruit been in the basket for over 3 days:')
    print(old_fruits_string + ' are over 3 days old.')


if __name__ == '__main__':
    print_fruit_statistics()
