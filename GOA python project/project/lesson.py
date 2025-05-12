task = [0]

while True:
    print("-1-choose action: ")
    print("1- add task: ")
    print("2- view list: ")
    print("3- mark as done: ")
    print("4- delete tasks: ")
    print("5- leave")
    choice = input("enter number: ")

    if choice == "1":
        print("add task: ")

    elif choice == "2":
        print("task list: ")

    elif choice == "3":
        print("mark task as done: ")

    elif choice == "4":
        print("Delete a task selected: ")

    elif choice == "5":
        print("program ended. goodbye ")
        break
    else:
        print("invalid choice! try again ") 


name = input("enter task name: ") 
task.append({"name": name, "done": False}) 
print("task added!") 


if not task:
    print("theres no task")
else:
    for i, task in enumerate(task):
     status = "W" if task["done"] else "X" 
     print(f"{i + 1}. {task['name']} [{status}]")  


index = int(input("which task you want to delete? enter number: ")) - 1
if 0 <= index < len(task):
    deleted = task .pop(index)
    print(f"task '{deleted['name']}' deleted.") 
else:
    print("incorrect number.") 



    
   
 
    