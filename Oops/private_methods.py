class Student:
    __name = "unknown"

    def __hello(self, name):
        self.__name = name
        print(self.__name)

    def welcome(self):
        print(Student.__name)
        self.__hello("chris")

s1 = Student()
s1.welcome()