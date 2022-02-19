x = 12
rev_num = 0
while x > 0:
    remainder = x % 10 
    rev_num = (rev_num * 10) + remainder
    x = x//10
print(rev_num)