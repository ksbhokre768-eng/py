a =input("enter a number :")
print(f"table of {a} is :")
try:
    for i in range(1 , 11):
        print(f"{int(a)} x {i} = {int (a)*i}") # still run if get an error
except Exception as e:
    print(e) 
    
print("HI")  

try:
    print("enter num")
    num=int((input()))
    a = [3, 4, 5]
    print(a[num])
except ValueError:   
    print( " not an intiger")

except IndexError:
    print("index not define")