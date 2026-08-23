class Account():
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

    def print_pass(self):
        print(self.__acc_pass)
a1=Account("123","asd")
a1.print_pass()
print(a1.acc_no)