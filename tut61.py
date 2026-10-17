class employee:
    def __init__(self , name , id):
        self.name=name
        self.id=id

    def showdetails(self):
        print(f"name of employee {self.id} is {self.name}")


class programmer(employee):
    def showlanguage(self):
        print("default language is python")  

e1=employee("rohan" ,400)
e2=programmer("arnav" , 345)
e1.showdetails()
e2.showdetails()
e2.showlanguage()           