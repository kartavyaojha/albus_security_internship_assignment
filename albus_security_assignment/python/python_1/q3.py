class Calculator:
    def __init__(self,num):
        self.num=num
    def square(self):
        return self.num**2
    def cube(self):
        return self.num**3

nym=7
calc=Calculator(nym)
print("Square of",nym,"is",calc.square())
print("Cube of",nym,"is",calc.cube())