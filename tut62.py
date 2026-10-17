# class employee:
#     def __init__(self):
#         self.__name="krishna"

# a=employee()
# # print(a.__name)# cannot be acess directly    //name mangling
# print(a._employee__name)# can be acess indirectly   

# print(a.__dir__())



class student:
    def __init__(self):
        self.name="krishna" 

    def _funname(self): #protected method
        return "code with harry"


class subject(student): #inherited class

    pass

obj=student()
obj1=subject()
print(dir(obj))

#calling object of student class

print(obj._name)
print(obj._funname())


# class employee:
#     pass

# a=employee()
# a.emp1=5