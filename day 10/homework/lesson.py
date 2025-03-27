#while loop გამოიყენება კოდის კონკრეტული ბლოკის გასამეორებლად რამოდენიმეჯერ სანამ პირობა არ დაკმაყოფილდება  # how does while loop work 

#თუ ჩვენ გვჭირდება loop ფიქსირებული რაოდენობის გაშვება ან რამის გაკეთება ერთხელ თითოეული ელემენტისთვის მაშინ ჩვენ ვიყენებთ for loop ამ მრიცხველზე დაფუძნებული ყველა ყველაფერი იყენებს for loop 
#თუ ჩვენ გვჭირდება ციკლი მანამ სანამ არ მოხდევა რაიმე კონკრეტული მდგომარეობა ან loop სამუდამოდ მაშინ გვსურს while loop- ი #whats the difference btw while loop and for loop 


password = ("paroli123") 

user_pass = (input("please enter the password: ")) 
while user_pass != password: 
    print("the password is incorrect please try again: ") 
    user_pass = (input("please enter the password: ")) 



#for i in range(1, 21, 2):
#    print(i) 