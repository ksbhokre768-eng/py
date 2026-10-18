class employee:
    def __init__(self ,name ):
        self.name=name


    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i


    def __str__(self):
        return f"the employee name is {self.name} str"

    def __repr__(self):
            return f"the employee name is {self.name} repr"
    
    def __call__(self):
         print("hello")
         
e=employee("harry")
print(e.name)
print(len(e))
