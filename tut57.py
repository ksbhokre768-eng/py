class person:
    name="harry"
    occupation="software developer"
    networth=1000

    def person(self):
        print(f"{self.name} is a {self.occupation}")

a=person()
b=person()
c=person()

a.name="krishna"
a.occupation="developer"

b.name="yash"
b.occupation="trader"

a.person()
b.person()
c.person()