with open('myfile text3', 'w') as f :
    f.write("hello world krishna here")
    f.truncate(12) # print only frist 12 letter
    

with open('myfile text3' , 'r') as f:
    print(f.read())
    f.seek(5) #skip frist 5 letter
    print(f.tell())#tell till where we seek
    x=f.read(6) # read letter after seek
    print(x)

