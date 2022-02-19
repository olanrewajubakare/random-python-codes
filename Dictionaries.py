# A dictionary is a data type for mutable objects that store mappings of unique keys to values
# Dictionary is mutable, unordered, and the keys can be used to index values, the keys are immutable and unique
# You must use immutable data types for the keys in a dictionary
elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
elements['lithium'] = 3
print(elements['helium'])
print('scandium' in elements)
print(elements.get('hydrogen'))
print(elements.get('scandium', 'there is no such element as scandium'))


animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3, 4, 2, 8, 2, 4], 'rabbits': [2, 3, 3],
           'fish': [0.3, 0.5, 0.8, 0.3, 1]}
print(animals['dogs'][3])
print(animals['fish'])
