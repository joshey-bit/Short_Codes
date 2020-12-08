m = int(input('enter m: '))
n = int(input('enter n: '))

# algorithm for gcd(n, m-n)
def gcd(m,n):
    if m < n: # assume m >= n
        (m,n) = (n,m)
    if (m%n) == 0:
        return(n) #this becomes gcd
    else:
        diff = m-n
        # but diff can be > n
        return(gcd(max(n,diff),min(n,diff)))

print(f'gcd of {m} and {n} is: ' + str(gcd(m,n)))

# simpler approach using while:
def hcf(m,n):
    if m < n:  # assume m >= n
        (m, n) = (n, m)
    while (m%n) != 0:
        diff = m-n
        # but diff can be > n
        (m,n) = (max(n,diff),min(n,diff))
    return (n)
print(f'hcf of {m} and {n} is: {hcf(m,n)}')

#algorithm using gcd(n,m%n) remainder approach
def g_c_d(m,n):
    if m < n:  # assume m >= n
        (m, n) = (n, m)
    if m%n == 0:
        return(n)
    else:
        return(g_c_d(n,(m%n)))  # as (m%n) < n always
print(f'g_c_d of {m} and {n} is: {g_c_d(m,n)}')

# using while
def h_c_f(m,n):
    if m < n:  # assume m >= n
        (m, n) = (n, m)
    while (m%n) != 0:
        (m,n) = (n,(m%n)) # as (m%n) < n always
    return (n)

print(f'h_c_f of {m} and {n} is: {h_c_f(m,n)}')

