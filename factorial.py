import math
def factorial(n):
    while n != 0:
        value = n * factorial(n-1)
        return(value)
    else:
        return(1)
    # if n <= 0:
    #     return(1)
    # else:
    #     value = n * factorial(n - 1)
    #     return(value)


n = int(input('enter the number: '))
print(math.log(factorial(n),100000000))
#print(factorial(n))

