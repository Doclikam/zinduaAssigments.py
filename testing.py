from collections import Counter

    
with open('text.txt','r') as file:
    number_of_lines=0
    number_of_words=0
    number_of_characters=0
    for line in file:
        number_of_lines+=1
        word_count=line.split()
        number_of_words=number_of_words+len(word_count)
        number_of_characters+=len(line)


   def frequent_word(file_name,words):
        content=file_name.read()
        words=content.split("")
        freq=dict()
        for word in words:
            if word in freq:
                freq[word]=1
                



        


    print( f" The number of lines is : {number_of_lines}") 
    print(f" The number of words is: {number_of_words}")
    print(f"The number of characters is: {number_of_characters}")
    print(x.most_common())  

