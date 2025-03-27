name = "Rati"

vowels = "a, e, i, o, u," 

vowels_letters = [letter for letter in name if letter in vowels] 


if vowels_letters:
    print("vowels", " ". join(vowels_letters))
else:
    print("names didnt found in vowels") 
