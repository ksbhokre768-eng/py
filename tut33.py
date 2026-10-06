dict= {
    "k" : "letter" ,
    "spoon": "obj" ,
    "lion":"king"                    
                    
}


print(dict["lion"])

for key in dict.keys():
    print(dict[key])

print(dict.keys())

print(dict.values())

print(dict.items())
for key , value in dict.items():
    print(f"for {key} value is {value}")
    print(f"for {key} value is {dict[key]}")