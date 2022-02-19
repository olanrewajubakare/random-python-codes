
def palindrome(x): 
    if x < 0: 
        return False
    return str(x) == str(x)[::-1]

num= int(input('Enter the number you want to check'))
print(palindrome(num))
