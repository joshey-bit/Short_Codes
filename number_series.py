def meth_1(n):
	diff = 1
	a0 = 1
	li = []	
	while n > 0:
		a_num = a0 + (n - 1)*diff
		n = n - 1
		li.insert(0, str(a_num))

	k = "".join(li)
	print(k)

def meth_2(n):
	diff = 1
	a0 = 1
	li = []
	num = 1	
	while num <= n:
		a_num = a0 + (num - 1)*diff
		num = num + 1
		li.append(str(a_num))

	k = ",".join(li)
	print(k)

n = input('enter the number: ')
meth_2(int(n))

#althogh method 1 is easy and memory efficient but it takes 0.4 sec to execute, method 2 takes 0.2sec


