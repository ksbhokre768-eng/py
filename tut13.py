a = "@@ harry @@@@@@@@"
print(len(a)) 
print(a.upper()) 
print(a.lower()) 
print(a.rstrip("@"))
print(a.replace("harry" , "john"))
print(a.split(" "))

heading = "introduction to js"
print(heading.capitalize())


str1 = "welcome to jungle!!!"
print(len(str1.center(50)))
print(len(str1))
print(str1.endswith("!!!"))

print(a.count("harry"))

print(str1.endswith("to",4,10))
print(str1[4:10])

str1 = "hello everyone"
print(str1.find("everyone"))
print(str1.find("everyone.."))
print(str1.index("everyone"))
# print(str1.index("everyone..")) to exit program

str1 = "welcome to jungle"
print(str1.isalnum()) #made of alpha numeric

str1 = "welcome to jungle"
print(str1.isalpha()) #only alphabets
print(str1.islower()) 
print(str1.isspace()) #only space
print(str1.istitle()) #if frist letter capital
print(str1.startswith("welcome"))
print(str1.swapcase())
print(str1.title()) #frist chr capital      