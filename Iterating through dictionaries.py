result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Iterate through the dictionary
for object, count in basket_items.items():
    if object in fruits:
        result += count

# if the key is in the list of fruits, add the value (number of fruits) to result


print(result)