'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. 
Store them in a list and find the score of the runner-up.

'''

k = [9,6,5,7,3,2,1,1,2,2,4,4,5,6,6,7,8,8,9]
without_duplicates = set(k)
listi = list(without_duplicates)
listi.sort()
print('the runner up is: ' +str(listi[-2]))



