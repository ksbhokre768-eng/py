import time
timestamp= time.strftime('%H:%M:%S')
print(timestamp)
timestamp= time.strftime('%H')
print(timestamp)
H = int(timestamp)
if(H<=12):
    print("good morning")
elif(H==12):  
     print("good afternoon")
elif(20>=H>=12):
     print("good evening")
else:
     print("good night")