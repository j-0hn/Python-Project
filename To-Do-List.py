print("\n----- TO DO LIST -----")

my_task = []

while True:
    print("1. Add Task\n2. View Task\n3. Remove Task\n4. Completed")
    option = int(input("\nWhat option: "))

    if option == 1:
        user_task = input("\nI need to ... ")
        user_status = input("Status of task: ")

        my_task.append({"task" : user_task, "status" : user_status})

        #for i in range(len(my_task)):
         #   print(my_task[i])
        for index, tasks in enumerate(my_task, start = 1):
            print("\nMy Task Now!")
            print(index, tasks["task"], tasks["status"],"\n")

    elif option == 2:
        print("*** View Task ***")
    elif option == 3:
        print("*** Remove Task ***")
    

print("Task Closed!")