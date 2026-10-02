l =[1, 2, 34, 1 , 1, 93 , 3, 4, 5, 6, ]
print (l)

l.append(7) #addition of num in list
print(l)

l.sort() #to sort list in ace order
print(l)

l.sort(reverse=True)  #also to sort list in dce order
print(l)

l.reverse()
print(l)

print(l.index(1))
print(l) 

print(l.count(1))
print(l) 

print(l.index(1))
print(l) 

l.insert(1,345)#insert 345 at index 1 of l
print(l)

m=l.copy()
m[0]=0
print(l)
print(m)

m=[345 , 876, 56]
l.extend(m)
k=l+m
print(k) # doesn't  changes l
print(l)