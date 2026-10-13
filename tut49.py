f = open ('pj.py' , 'r') #reading this mode open file for reading only it is a default mode and throws error if file doesn't exxist 
# f = open ('pj.py' , 'w') # writing this mode opens the file for writing only and creates new file if doesnt exixt 
# f = open ('pj.py' , 'a') # appeding  opens file for appending  and creaates new if doesnt exist
# b as binary file 
# x create file and gives an error if file already exist
# f.write() to write

# if  we use with staement then we dont needd to close file
text = f.read()
print(text)
f.close()