class student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def display(self):
      #  print(f"{self.name} {self.age}")
        

s1 = student("John", 20)
s2 = student("Isabek", 19)
s3 = student("Bianca", 20)

# s1.display()
# s2.display()
# s3.display()

# print(student_one.name)
# print(student_one.age)

print(s1.name)
print(s2.age)
print(s3.name)


class Person():
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def greet(self):
		print(f"Hello, my name is {self.name}")

p1 = Person("John", 36)
p1.greet()

# Create the Dog class
class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def bark(self):
    print(self.name + " says Woof!")

# Create an object
d1 = Dog("Buddy", 3)

# Call the bark method
d1.bark()