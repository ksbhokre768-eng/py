#MAP
def cube(x):
    return x*x*x

l=[1,2,3,4,5]
newl=[]
# for i in l:
#     newl.append(cube(i))

newl=list(map(cube,l))

print(newl)

#FILTER
def filter_fn(a):
    return a>4

newnewl=list(filter(filter_fn ,l))

print(newnewl)

from functools import reduce
numbers=[1,2,3,4,5,6]
def mysum(x,y):
    return x+y

sum=reduce(mysum , numbers)
print(sum)