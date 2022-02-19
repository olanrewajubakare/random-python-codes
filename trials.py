def palindrome(x): 
    if x < 0: 
        return False
    value = x
    rev_num = 0 
    while x > 0:
        remainder = x % 10 
        rev_num = (rev_num * 10) + remainder
        x = x//10
    return rev_num == value

num= int(input('Enter the value to check'))
print(palindrome(num))
