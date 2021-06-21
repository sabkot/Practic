from random import randint
lst = [randint(-100, 100) for i in range(30)]
print (lst)
max_el = max(lst)
print(max_el)
s = 0
max_index = 0
for x in range (len(lst)):
    if lst[x] > s:
        s = lst[x]
        max_index = x
print (max_index)
for i in range (len(lst)-1):
    print(lst[i],lst[i+1]) if lst[i]<0 and lst[i+1]<0 else None

