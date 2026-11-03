import random
print("***** Math Game ***** \n")

class Question:
    def __init__(self, num1=1, num2=10):
        self.num1 = random.randint(num1, num2)
        self.num2 = random.randint(num1, num2)
        self.answer = None

    def addition(self):
        self.answer = self.num1 + self.num2
        return f"What is {self.num1} + {self.num2} ?"

    def subtraction(self):
        self.answer = self.num1 - self.num2
        return f"What is {self.num1} - {self.num2} ?"

    def multiply(self):
        self.answer = self.num1 * self.num2
        return f"What is {self.num1} * {self.num2} ?"

    def divide(self):
        self.answer = self.num1 / self.num2
        return f"What is {self.num1} / {self.num2} ?"

class Player:
    def __init__(self, codename, score=0):
        self.codename = codename
        self.score = score

player_name = Player(input("Enter your codename: "))
print(f"Welcome {player_name.codename} to the Game! \n")
print(f"Your current score is: {player_name.score} \n")



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

if operator_choice in operator(): # to match the choice to functions operator()
    print(operator()[operator_choice]()) # to print the question in every operator
    guess_ans = int(input("Your answer: "))
    if guess_ans == question.answer: # question.answer to get the total answer in every questions
        print("Tama!")
    else:
        print("Mali!")
else:
    print("Invalid choice!")

