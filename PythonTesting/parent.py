class Calculator:
    num = 100

    def __init__(self, a, b):
        self.a= a
        self.b= b
        print("Called automatically when obj created")

    def get_data(self):
        print("Method in class")

    def summation(self):
        return self.a + self.b + Calculator.num

obj = Calculator(2, 3)
obj.get_data()
print(obj.summation())

obj = Calculator(4, 5)
obj.get_data()
print(obj.summation())