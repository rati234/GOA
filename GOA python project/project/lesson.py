# task = [0]

# while True:
#     print("-1-choose action: ")
#     print("1- add task: ")
#     print("2- view list: ")
#     print("3- mark as done: ")
#     print("4- delete tasks: ")
#     print("5- leave")
#     choice = input("enter number: ")   
#     if choice == "1":
#         print("add task: ")

#     elif choice == "2":
#         print("task list: ")

#     elif choice == "3":
#         print("mark task as done: ")

#     elif choice == "4":
#         print("Delete a task selected: ")

#     elif choice == "5":
#         print("program ended. goodbye ")
#         break
#     else:
#         print("invalid choice! try again ") 


# name = input("enter task name: ") 
# task.append({"name": name, "done": False}) 
# print("task added!") 


# if not task:
#     print("theres no task")
# else:
#     for i, task in enumerate(task):
#      status = "W" if task["done"] else "X" 
#      print(f"{i + 1}. {task['name']} [{status}]")  


# index = int(input("which task you want to delete? enter number: ")) - 1
# if 0 <= index < len(task):
#     deleted = task .pop(index)
#     print(f"task '{deleted['name']}' deleted.") 
# else:
#     print("incorrect number.") 



# num1 = int(input("please enter the number: "))

# if num1 % 2 == 0:
#     print("number is even")
# else:
#     print("number is odd")


# num1 = int(input("please enter number: "))

# num2 = 23

# while num1 == num2:
#     print("true") 
# while num1 != num2:
#     print("true")




# def find_primes():
#     primes = []
#     for num in range (1,30):
#         if num > 1:
#             for i in range(2, num):
#                 if num % i == 0:
#                     break
#                 else:
#                     primes.append(num)
#                     return primes
#                 print(find_primes)  
   

# num = [3, 15, 7, 12, 42] 

# def find_max(num):

#     max_number = num[0]

#     for num in num:
#         if num > max_number:
#             max_number = num

#     return max_number 

# print(find_max(num)) 


# nugzar_chubiridze = (4,3)


# def nugzar_chubiridze(sadghegdzelo, limit):
#     if sadghegdzelo > limit:
#         return f"luiza: nugzar aghar dalio meti!"
#     else:
#         return f"axla martla {limit} damilocne"
# print(nugzar_chubiridze(4,3)) 
# yuri_gagarini_pressure_ = 120
# yuri_pulse = 80

# def yuri_gagarini(yuri_gagarini_pressure, yuri_pulse):
#     pressure = int(input("ramdenia sheni gulis wneva?: "))
#     pulse = int(input("ramdenia sheni pulsi?: "))

#     if pressure == 120: 
#         return True   
#     else:
#         return False
    
# print(yuri_gagarini(120, 80))  


def captainjack():
    gold_coin = int(input("sheiyvane oqros monetebis raodenoba"))

    if gold_coin == 0:
        
        return
    
    

print("airchoi gemi miutite pasi")
print("1) 150 coin")
print("2) 200 coin")
print("3) 250 coin")
print("5) 300 coin")

ship_price = int(input("airchie gemis pasi: "))

if gold_coin >= ship_price:
    print("gemi warmatebiT sheidzina")





