num = (2 , 4 , 67, 89 ,56, 4)
print(num)
print(num.count(4))
print(num.index(4))
print(num.index(4,2,6))#gives index in slice we choose
print(len(num))
temp=list(num)
print(temp)

temp.append(546)  #add
print(temp)

temp.pop(4) #remove
print(temp)

num = tuple(temp)
print(num)      

tup1=(546,)
tup2=(5467,)# if comma is not present it become int

tup3=tup1+tup2
print(tup3)