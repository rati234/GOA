# ფუნქციები გვჭირდება რომ კომპიუტერს მივანიშნოთ თუ რისი გაკეთება გვსურს და ასევე ვიყენებთ თუ მისი გამეორებაც გვინდა რამდენიმეჯერ ეს ნიშნავს რომ ფუნქცია არის კოდის ნაწილი 

def double_values(list):
     new_list = [1, 2, 4, 5, 6, 7, 8, 9, 10] 
     for numbers in new_list:  
         doubled = 1 * 2, 2 * 2 , 4 * 2 , 5 * 2 , 6 * 2 , 7 * 2, 8 * 2, 9 * 2, 10 * 2 
         new_list.append(doubled)
         return new_list
    

 

doubled_number = double_values(list)    
print(doubled_number) 




