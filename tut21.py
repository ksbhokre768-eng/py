def average (a=4,b=8):
    print("the value ofaverage" , (a+b)/2)
# average  (4,5)   
# average()#use default values
average(b=9)

def name(fname  , mname="shailesh" , lname="bhokre" ):
    print ("hello" , fname , mname , lname )

name ("krishna") 


def mean(*num):
    sum=0
    for i in num:
        sum=sum+i
    # print ("average of numbers" , sum/len(num))
    # return 7
    return sum/len(num)
c=mean( 2, 5 ,6 )  
print(c) 