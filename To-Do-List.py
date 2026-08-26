print("----- TO DO LIST -----")

my_task = []

print("1. Add Task")
user_task = input("I need to ... ")
my_task.append(user_task)
for task in range(len(my_task)):
    print(my_task[task])