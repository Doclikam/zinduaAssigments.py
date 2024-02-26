
import random
while allowed_attempts>0:
    guess=input('enter a letter: ').upper()
    

    if guess.upper() in word.upper():
        print('Good job!')
    else:
        allowed_attempts-=1
        print(f"The letter is not in the word. {allowed_attempts} remaining attempts")
        

    guesses= guesses+guess
    wrong_letter_count=0  
    for letter in word:
        if letter.upper() in guesses:
            print(letter, end="")
        else:
           wrong_letter_count+=1
           print("_", end="")   
    print("")  

    if wrong_letter_count==0:
        print(f"You won! secret word is {word}") 
        break
    
else:   
        print('You lost')
