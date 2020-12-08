# to find position of elements in the list
# 1st algorithm
# to check wheter a value exist in lista and note its first position, if value doesnot exists return -1

def find_position(l,v):
    (found, i) = (False, 0)
    while i < len(l):
        if l[i] == v and not found:
            (found, pos) = (True, i)
        i = i+1
    if not found:
        pos = -1
    return(pos)

# method 2
def find_pos(l,v): # l = list, v = value
    (pos, i) = (-1, 0)
    for x in l:
        if x == v:
            pos = i
            break
        i = i+1
    return(pos)

# method 3
def find_poss(l,v):
    for i in range(len(l)):
        if l[i] == v:
            pos = i
            break
    else:
        pos = -1
    return(pos)

l = list('abcdefghijklmnopqrstuvwxyzh')
v = 'h'
print(l)
print(find_position(l,v))

