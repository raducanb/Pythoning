# class MyClass: 
#     x = 10 
#     y = 20
#     def Test(self,value):
#         return ((self.x+self.y)/2 == value)

# class AnotherClass:
#     def MyFunction(self,v1,v2):
#         return str(v1+v2)+" - "+str(self.x)+","+str(self.y)
 
# m = MyClass()
# print (m.Test(15),m.Test(16)) 
# m.Test = AnotherClass().MyFunction 
# print (m.Test(1,2))

class MyClass: 
    x = 10
    def Test(self,value):
        return ((self.x+self.y)/2 == value)
    def MyFunction(self,v1,v2):
        return str(v1+v2)+" - "+str(self.x)

m = MyClass()
m2 = MyClass()
m2.x = 100
m.Test = m2.MyFunction 
print (m.Test(1,2))
print (m.MyFunction(1,2))

# class Point:
#     def __init__(self):
#         self.x = 10
#         self.y = 10

# p = Point()
# print(p.x)

#equivalent with

def PointClass__init__(obj):
    obj["x"] = 10
    obj["y"] = 10
Point = {"__init__": PointClass__init__}
p = dict(Point)
p["__init__"](p)
print(p["x"])