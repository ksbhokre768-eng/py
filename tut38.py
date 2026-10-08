def func():
    a= input("enter value bet 5 and 9 ")
    if(a=="quit"):
        return "quit"
    if(a==str):
        raise SystemError( "string not define")
    if(int(a)<5 or int(a)>9):
        raise ValueError("error value not define")
    else:
        return a

x =func()
print(x)    