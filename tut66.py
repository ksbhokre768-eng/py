class employee:
    employeeno=0
    companyname="apple"
    def __init__(self , name):
        self.name=name
        self.raize= 0.5
        employee.employeeno +=1

    def showdetail(self):
        print(f"the name is {self.name} and the raise amount in {self.employeeno} sized {self.companyname} is {self.raize}")

e1=employee("harry")
e1.raize=0.4
e1.companyname=("google")
e1.showdetail()
e2=employee("rohan")
e2.showdetail()
