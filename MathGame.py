import random

print("***** Math Game ***** \n")

class Question:
    def __init__(self, num1=1, num2=10):
        self.num1 = random.randint(num1, num2)
        self.num2 = random.randint(num1, num2)

    def addition(self):
        return f"What is {self.num1} + {self.num2} ?"

    def subtraction(self):
        return f"What is {self.num1} - {self.num2} ?"

    def multiply(self):
        return f"What is {self.num1} * {self.num2} ?"

    def divide(self):
        return f"What is {self.num1} / {self.num2} ?"


question = Question()

def operator():
    operations = {
        1: question.addition,
        2: question.subtraction,
        3: question.multiply,
        4: question.divide
    }
    return operations

operator_choice = int(input("Choose an operation \n1: Addition\n2: Subtraction\n3: Multiplication\n4: Division:\n -> "))

if operator_choice in operator():
    print(operator()[operator_choice]())
else:
    print("Invalid choice!")

