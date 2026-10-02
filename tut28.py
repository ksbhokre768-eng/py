letter = "hey my name is {} and I am from {}"
name = "Krishna"
country= "India"

print(letter.format(name,country))

print(f"Hey my name is {name} and I am from {country}")
print(f"Hey my name is {{name}} and I am from {{country}}")#print as it is

txt =("the value of doller is {price:.2f}")#only take 2 dce places

print(txt.format(price=98.09126))