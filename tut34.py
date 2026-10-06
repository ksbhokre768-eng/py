ep = { 342: 56 , 634: 54 , 453:87} 

ep1={111:78 , 222:68}

ep.update(ep1)
print(ep)

# ep.clear()
empt={}
print(ep)
print(type(empt)) 
ep.popitem(342)
del ep