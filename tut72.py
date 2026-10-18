class parent:
    def parent_method(self):
        print("this is parent class")

class child(parent):
    def parent_method(self):
        print("harry")
        super().parent_method()
    def child_method(self):
        print("this is child claas ")
        super().parent_method()

child_object=child()
child_object.child_method()
child_object.parent_method()

