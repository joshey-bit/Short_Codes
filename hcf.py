# program for hcf
m = int(input('enter m: '))
n = int(input('enter n: '))

def hcf(m,n):
    # create list for factors of m
    fm = []
    for i in range(1,m+1):
        if (m%i) == 0:
            fm.append(i)
    # create list for factors of n
    fn = []
    for j in range(1,n+1):
        if (n%j) == 0:
            fn.append(j)
    # create list for commpn factors
    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)
    print(f'the factors of {m}: {fm}')
    print(f'the factors of {n}: {fn}')
    print('the hcf of '+ str(m)+ ' and ' + str(n)+ ' is '+ str(cf[-1])) #the hcf of two no.s

print(hcf(m,n))

# simpler version of above program
def gcd(m,n):
    cf = []
    for i in range(1, min(m,n)+1):
        if (m%i) == 0 and (n%i) == 0:
            cf.append(i)
    print(f'the gcd of {m} and {n} is: {cf[-1]}') #formated for hcf printing

print(gcd(m,n))

# version without having lists
def h_c_f(m,n):
    for i in range(1, min(m,n)+1):
        if (m%i) == 0 and (n%i) == 0:
            mrcf = i  #mrcf = most recent common factor
    print(f'the h_c_f of {m} and {n} is: {mrcf}')

print(h_c_f(m,n))

# approach using while loop and consider from min(m,n) to 1, reverse order for simplififcation
def g_c_d(m,n):
    i = min(m,n)
    while i>0:
        if (m%i) ==0 and (n%i) ==0:
            return(i)
        else:
            i -= 1

print(g_c_d(m,n))

