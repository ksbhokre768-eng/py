def func():
    try:
        l=[1, 2, 3,4]
        i = int(input("value of i is"))
        print(l[i])
        return 1
    
    except:
        print (" an error occour")
        return 0 
    finally: # use in fn specially because afterreturn value fn doesn't exicute
        print("line always exicute")
         
x = func()
print(x)     