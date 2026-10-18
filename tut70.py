class employee:
    def __init__(self , name , salary):
        self.name=name
        self.salary=salary



    @classmethod
    def fromstr(cls , str):
        return cls(str.split("-")[0] , str.split("-")[1])


e1="john-12000"
e=employee.fromstr(e1)
print(e.name)
print(e.salary)
        