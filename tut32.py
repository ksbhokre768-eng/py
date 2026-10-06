s ={1, 2 , 3, 4}
s1={1, 2 ,6 , 7,8 ,89 }
print(s.union(s1))
print(s.intersection(s1)) 
s.intersection_update(s1)
print(s)
print(s.symmetric_difference(s1)) 
print(s.difference(s1))# i update set

s3={1, 2, 3, 4}
s4={5, 6, 7, 8}
print(s3.isdisjoint(s4)) 

print(s1.issuperset(s))
print(s.issubset(s1))
s. add(4)
print(s)

s.discard(4)
print(s)

item = s1.pop()
print(item)

del s # delete s
s1.clear() #clear all elements
print(s1)