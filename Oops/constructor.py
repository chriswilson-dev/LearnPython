class Student():
        def __init__(self):
            print("adding new student to database..")
#__init__() is a special method that Python calls automatically 
# when an instance of a class is created. 
# You don't have to define it yourself. 
# If you don't define one, Python uses the inherited/default 
# initialization behavior.
# Python essentially makes the current object available to 
# __init__() through self.
s1=Student()
#self is not a pre-defined keyword
#It is a conventional parameter name used to 
# refer to the current instance.