class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)
class student(Person):
    def __init__(self,fname,lname,year):
        super(). __init__(fname,lname)
        self.graduation = year
x = student ("Joey","King",2021)
x.printname()
print(x.graduation)
