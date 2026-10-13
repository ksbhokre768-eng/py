f = open('myfile.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"mark of student {i} in maths is : {m1}")
    print(f"mark of student {i} in sst is : {m2}")
    print(f"mark of student {i} in eng  is : {m3}")

    print (line)


j=open('myfile2.txt','w')
lines = ['line1\n' ,' line2\n' ,' line3\n']
j.writelines(lines)
f.close()