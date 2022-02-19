datestr = '1956-01-31'
year, month, day = datestr.split('-')
print(year)
"""str.join() takes us in the other direction, sewing a list of strings up into one long string, 
using the string it was called on as a separator."""
print('?'.join([year, month, day]))