class employee:
    def __init__(self , name , id):
        self.name=name
        self.id=id

class programmer(employee):
    def __init__(self, name, id , lang):
        self.lang=lang
        super().__init__(name, id)
    def show(self):
        print(f"employee name is {self.name} his id is {self.id} and use language {self.lang}")
e=programmer("harry" , 345 ,"python")
print(e.name)
print(e.id)
print(e.lang)
e.show()