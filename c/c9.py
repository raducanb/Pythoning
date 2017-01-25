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