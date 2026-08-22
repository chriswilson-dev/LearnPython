class Student():
    #default constructors
    def __init__(self):
        pass
    #parameterized constructors
    def __init__(self, name, age, marks):
        self.name=name
        self.age=age
        self.marks=marks

class Students():
    college="ABC college"       #class attribute
    name="unknown"
    def __init__(self,age):     #instance attribute
        self.age=age            
s1=Students(22)
print(s1.name)                  #class.attr<<obj.attr