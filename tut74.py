class shape:
    def __init__(self ,x ,y):
        self.len=x
        self.brd=y
    def area(self):
        return self.len*self.brd
class circle(shape):
    def __init__(self, r):
        self.red=r
        # super().__init__(r, r)

    def area(self):
        return 3.14 *self.red*self.red

c=circle(7)
print(c.area())    
rec=shape(3,5)
print(rec.area())