import time
timestamp= time.strftime('%H:%M:%S')
print(timestamp)
timestamp= time.strftime('%H')
print(timestamp)
a=(input("enter your name:" ))
print(a)
H = int(timestamp)
if(H<=12):
    print("good morning",a)
elif(H==12):  
     print("good afternoon",)
elif(20>=H>=12):
     print("good evening",a)
else:
     print("good night",a)