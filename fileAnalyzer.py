#importing counter will assist in finding the most common word 
from collections import Counter

def file_content(file_name, file_mode):
    try:
        with open(file_name,file_mode) as file:
            number_of_lines=0
            number_of_words=0
            number_of_characters=0
            for line in file:
                number_of_lines+=1
                words=line.split()
                number_of_words=number_of_words+len(words)
                number_of_characters+=len(line)
                avg_words=round(number_of_characters/number_of_words)
                counts=Counter(words)
                mostcommon=counts.most_common(4)
                

        print( f" The number of lines is : {number_of_lines}") 
        print(f" The number of words is: {number_of_words}")
        print(f"The number of characters is {number_of_characters}")
        print(f"The average word length is: {avg_words} ")
        print(f"The most common word is {mostcommon}")


    except FileNotFoundError:
        print(f'{file_name} not found!')
        return 0

    



file_name=input('Enter the name of the file:').lower()
file_mode=input("what mode would you like to open with 'r' or 'w': ").lower()
 
file_content(file_name,file_mode)

