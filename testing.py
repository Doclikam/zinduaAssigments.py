#importing counter will assist in finding the most common word 
from collections import Counter


with open('text.txt','r') as file:
    number_of_lines=0
    number_of_words=0
    number_of_characters=0
    word_count={}
    for line in file:
        number_of_lines+=1
        words=line.split()
        number_of_words=number_of_words+len(words)
        number_of_characters+=len(line)
        
        
    print( f" The number of lines is : {number_of_lines}") 
    print(f" The number of words is: {number_of_words}")
    print(f"The number of characters is: {number_of_characters}")
    print(f"The most common word is {mostcommon}")

