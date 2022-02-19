expense = {'January': 2200,'February': 2350,'March': 2600,'April' : 2130,'May': 2190}

print(expense['February'] - expense['January'])
print(expense['January'] + expense['February'] + expense['March'])
for key, values in expense.items(): 
    is_2000 = False 
    if values == 2000:
        is_2000 = True
    print(is_2000)
    
expense['June'] = 1980
print(expense)
expense['April'] -= 200
print(expense)