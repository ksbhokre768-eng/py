i = input("choose any one snake , water , gun :")
if i=="snake" :
    k=0
if i=="water" :
    k=1
if i=="gun" :
    k=2
print("computer chooses")
import random
j=''.join(random.sample('012' ,1))
j=int(j)
if j==0 :
    print("snake")
if j==1:
    print("water")
if j==2:
    print("gun")

if j==k :
    print("draw")

elif j>k:
    print("you loose")

else:
   print ("you won")                      