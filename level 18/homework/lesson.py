# ჩვენ ლეველ 18 გაკვეთილზე ვისწავლეთ remove ფუნქცია და count ფუნქცია ასევე extend ფუნქცია 


#HOW DOES REMOVE FUNCTION WORK FOR EXAMPLE:

# fruits = ["apple", "banana", "watermelon"] 

# fruits.remove("banana") 

# print(fruits) 

#how does count work for example : 

# txt = "i love apples, apple is my favorite fruit"

# x = txt.count("apple") 

# print(x)  


# user_list = []


# input("please enter numbers in the list") 


# print("Enter items to add to the list:")



# user_list = [] 

# input("please enter numbers in the list") 

# print("Enter items to add to the list:")

# for i in range(n): 
#     a.append(int(input()))
# for i in range(n):
#     if a[i] not in a[:i]:
#         if a.count(a[i]) > 1:
#             print(a[i], a.count(a[i]))



n = int(input("enter a number"))
a = []
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if a[i] not in a[:i]:
        if a.count(a[i]) > 1:
            print("რიცხვი", a[i], "მეორდება", a.count(a[i]), "ჯერ")


