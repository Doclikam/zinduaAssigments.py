#importing counter will assist in finding the most common word 
from collections import Counter

#function to allow user to input file name and opening mode
def file_content(file_name, file_mode):
    #the try-exception catches any error when a file cannot be found or opened. 
    try:
        with open(file_name,file_mode) as file:
            number_of_lines=0
            number_of_words=0
            number_of_characters=0 
            #for each line in the file
            for line in file:
                #increaments the line by one in the next iteration
                number_of_lines+=1
                #separate words by spaces into a list
                words=line.split()
                #count the number of words
                number_of_words=number_of_words+len(words)
                number_of_characters+=len(line)
                avg_words=round(number_of_characters/number_of_words)
                #counter to count the frequency of the most common words
                counts=Counter(words)
                mostcommon=counts.most_common(1)
                

        print( f" The number of lines is : {number_of_lines}") 
        print(f" The number of words is: {number_of_words}")
        print(f"The number of characters is {number_of_characters}")
        print(f"The average word length is: {avg_words} ")
        print(f"The most common word is {mostcommon}")
fi
    
        #creating a new file to write the results of the anlysis
        with open ("analysis.txt", "w") as analysis:
            analysis.write(f"Number of lines:{number_of_lines}\n")
            analysis.write(f"Number of words: {number_of_words}\n")
            analysis.write(f"Number of characters: {number_of_characters}\n")
            analysis.write(f"Average word length: {avg_words}\n")
            analysis.write(f"Most common word: {mostcommon}\n")




   #the error is thrown when the file given is not found.
    except FileNotFoundError:
        print(f'{file_name} not found!')
    
        return 0

    
#use input
file_name=input('Enter the name of the file:').lower()
file_mode=input("what mode would you like to open with 'r' or 'w': ").lower()
 #calling the function
file_content(file_name,file_mode)




    
