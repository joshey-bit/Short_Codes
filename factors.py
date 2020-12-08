def factors(n):
    l = []
    for i in range(1, n+1):
        if n%i == 0:
            l.append(i)
    return(l)
# to check whether no. is prime
def isprime(n):
    return (factors(n) == [1,n])

# to list out prime no.s upto n
def prime_upto(n):
    prime_list = []
    for i in range(1, n+1):
        if isprime(i):
            prime_list.append(i)
    return(f'the prime no.s upto {n} are: {prime_list}')

# to determine frst n prime no.s
def nprime(n):
    (count, i, p_list) = (0, 1, [])
    while count < n:
        if isprime(i):
            (count, p_list) = (count + 1, p_list + [i])  # here p_list.append(i) doesnt give value as list is in tuple and it cannot be mutable, by + it creates new list
        i = i + 1
    return(f'the first {n} prime no.s are: {p_list}')

n = int(input('entern the no,: '))
print(nprime(n))