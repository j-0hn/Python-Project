class student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"{self.name} {self.age}")
        

s1 = student("John", 20)
s2 = student("Isabek", 19)
s3 = student("Bianca", 20)

s1.display()
s2.display()
s3.display()

#print(student_one.name)
#print(student_one.age)


