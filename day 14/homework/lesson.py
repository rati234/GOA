name = "Rati"

vowels = "a, e, i, o, u," 

vowels_letters = [letter for letter in name if letter in vowels] 


if vowels_letters:
    print("vowels", " ". join(vowels_letters))
else:
    print("names didnt found in vowels") 


სტრინგები უცვლელია (immutable)  რადგან როცა სტრინგს ქმნი ის მეხსიერებაში ინახება ისე რომ მისი ცალკეული სიმბოლოები შეცვლადი არარის 


სიები (LIST) ცვლადია რადგან სია არის ისეთი მონაცემთა სტრუქტურა სადაც ელემენტების პირდაპირი ცვლილება შეგვიძლია 

list = [] 

for _ in  range (8):
    value = input("please enter your name and surname: ")
    value = input("age: ")
    value = input("date of birth: ") 
    value = input("height and your living adress: ")
    value = input("what sport you like and whats your job: ") 
    list.append(value) 
    print("your input is:", list) 



numbers = []   

for _ in range(10):
    meaning = int(input("please enter a meaning: ")) 
    numbers.append(meaning) 
print("your entered information") 

for num in numbers: 
    if num % 2 == 0: 
        print(f"{num} - evem") 
else:
    print(f"{num} - odd"


num1 = int(input("please enter the number: "))

num2 = int(input("please enter the number: "))

operation = input("please enter operation: ") 


def calculator(num1, num2, operation):
    if operation == '+':
        return  num1 + num2
    elif operation == '-':
        return  num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return  num1 / num2
    elif num2 == 0 and operation == "/":
         return  " incorrect: we cant division numbers to zero "   


print (calculator(num1, num2, operation))

