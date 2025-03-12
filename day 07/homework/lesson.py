#A- True True False False 
#B- true false true false 
#A and B - true false false false 

print(True and False or True or True and False)  

num1 = float(input("please enter first number: "))  #მომხმარებელს ვთხოვ რომ თავისი პირველი რიცხვი შემოიტანოს
num2 = float(input("please enter second number: ")) #ანალოგიური როგორც ზემოთა ხაზში ვატანინებ მე-2 რიცხვს

if num1 > 0:  
    print("this number is a True: ") #თუ ნამ1 მეტია 0-ზე პასუხი უნდა იყოს დადებითი
elif num1 == 0:
    print("the number is a zero") # ამით ვამოწმებთ არის თუ არა ორი მნიშვნელობა ტოლი
else:
    print("this number is a False") # ამით პროგრამას ვეუბნებით რომ თუ რიცხვი ნაკლებია 0-ზე დაწეროს რომ ეს რიცხვი არის უარყოფითი

#მე-4 დავალება 


num1 = int(input("please enter your rating score: ")) #მომხმარებელს ვთხოვ შემოიტანოს მისი შემაფასებელი ქულა

if num1 >= 90:
    print("Grade A")  #ვეუბნებით პროგრამას თუ რიცხვი მეტია ან ტოლია 90-ის დაპრინტოს გრეიდ ა 
if num1 >= 70:
    print("Grade B") #თუ მეტია ან ტოლია 70-ზე დაწეროს გრეიდ ბ
if num1 >= 50:
    print("Grade C") #თუ მეტია ან ტოლია 50 ის დაწეროს გრეიდ ცი
else:
    print("Grade F") #ყველა სხვა შემთხვევაში კი გრეიდ ფ


num1 = int(input("please enter number: ")) #ვატანინებ მომხმარებელს რიცხვს

if num1 % 2 == 0 and num1 > 10:  #თუ ეს რიცხვი არის ლუწი და ამავდროულად მეტია 10-ზე დაბეჭდოს რომ ეს რიცხვი არის დადებით ანუ True
    print("this number is a True ") 
else:
    print("this number is a False ")    #ყველა სხვა შემთხვევაში კი დაბეჭდოს რომ ეს რიცხვი არის უარყოფითი
