'''program to return a list such that
x + y + z != n

[i,j,k] shuch that i + j + k != n
0<=i<=x, 0<=j<=y, 0<=k<=z

'''

x = int(input('enter x: '))
y = int(input('enter y: '))
z = int(input('enter y: '))
n = int(input('enter n: '))

#the condition:
#x+y+z != n

check_list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k != n)]
print(str(check_list))
