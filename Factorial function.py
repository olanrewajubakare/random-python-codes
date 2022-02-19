def factorial(n):
    fac = 1
    if n < 0:
        print('positive numbers only')
    elif n == 0:
        print('the factorial of 0 is 1')
    else:
        for i in range(1, n+1):
            fac = fac * i
        return fac

print(factorial(7))
