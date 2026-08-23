class Student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def print_avg(self):
        print(sum(self.marks)/len(self.marks))
s1=Student("Chris",[98,92,93])
s1.print_avg()
