def addTask():
    task = input("please Enter a Task")
    tasks.append(task)
    print(f"task'{task}' added to the list.")
   
def listTasks():
    if not tasks:
        print("there are no tasks currently!")
    else:
        print("current task:")
        for index, task in enumerate(tasks):
            print(f"task #{index}. {task}")
           
def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("choose the number of the task you want to delete:"))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"task {taskToDelete} has been removed.")
        else:
            print(f"task #{taskToDelete} was not found.")
    except:
        print("Invalid input. please try again.")S
print("welcome to TO-DO LIST App")
while True:
    print("\n")
    print("please select one of the following options")
    print("---------------------------------------")
    print("1. Add a task")
    print("2. Delete a task ")
    print("3. List task")
    print("4. Quit")
               
    choice = input("enter your choice:")
               
    if(choice == "1"):
        addTask()
    elif(choice == "2"):
        deleteTask()
    elif(choice == "3"):
        listTasks()
    elif(choice == "4"):
        break
    else:
        print("Invalid input. Please try again")
                   
print("Goodbye!")
