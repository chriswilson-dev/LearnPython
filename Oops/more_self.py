class Student():
    def __init__(self,fullname):
        self.name=fullname
        print("adding student")
s1=Student("karan")
print(s1.name)
#Here the input parameter is called fullname,
#but the attribute stored in the object is called name.