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
class tringle (geometry):
    def __init__(self, area,perimeter):
        super().__init__(area,perimeter)
a=int(input("enter a altitude of the triangle:"))
b=int(input("enter a base of the triangle:"))
c=int(input("enter a side of the triangle:"))
d=int(input("enter a side 2 of the triangle:"))
area=1/2*a*b
perimeter=b+c+d
print(area)
print(perimeter)