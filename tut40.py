import random
print("choose 1 for code and 2 for decode")
i=int(input(" "))
a = input("enter your massege: ")
if i==1:    
    for str in a.split():
        if len(str) >=3 :
        # print(str[2] + str[0] + str[1])
        # str=list[str]
             start = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz' , 3))
             end = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz' , 3))
             print(start +str[-1]+str[:-1]+ end , end=" ")
        else:
            print(str[::-1] , end=" ")    
    # print(''.join(str))

# decode 

if i==2:
    for str in a.split():
        if len(str) >=3 :
            print(str[4:-3]+str[3] , end=" ")
        else:
            print(str[::-1] , end=" ")
# i=int(input())
# if i==1:
