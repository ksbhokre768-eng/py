class employee:
    companyname="apple"
    def __init__(self,name):
        self.name=name

    def show(self):
        print(f"the name is {self.name} and company is {self.companyname}")

    @classmethod
    def changecompany(cls , newcompany):
        cls.companyname=newcompany

e1=employee("harry")
# e1.name="harry"
e1.show()
e1.companyname="tesla"
e1.show()
print(employee.companyname)