marks =[1,3 , 4, 5, 6, 7,8 ,9]

index=0
for mark in marks :
    print(index)
    if index==3:
        print("hi")
    index +=1


for index , mark in enumerate (marks , start=2):
    print(mark)
    if index==3:
        print("hi")


