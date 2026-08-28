class Student:
    __name = "unknown"          # Private class attribute

    def __hello(self, name):    # Private method
        self.__name = name      # Store value in this object's private attribute
        print(self.__name)      # Print object's private attribute

    def welcome(self):
        print(Student.__name)   # Access class attribute → "unknown"
        self.__hello("chris")   # Call private method → "chris"

s1 = Student()                  # Create Student object
s1.welcome()                    # Call public method from outside