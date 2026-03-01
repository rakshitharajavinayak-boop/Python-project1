class geometry:
    def __init__(self,area,perimeter):
        self.area=area
        self.perimeter=perimeter

class square (geometry):
    def __init__(self, area,perimeter):
        super().__init__(area,perimeter)
a=int(input("enter a side of the square:"))
area=a*a
perimeter=a*4
print(area)
print(perimeter)
class rectangle (geometry):
    def __init__(self, area,perimeter):
        super().__init__(area,perimeter)
a=int(input("enter a lenght of the rectangle:"))
b=int(input("enter a bredth of the rectangle:"))

area=a*b
perimeter=a+a+b+b
print(area)
print(perimeter)