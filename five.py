import nltk

# Download the English dictionary from nltk
nltk.download('words')

# Load the English dictionary
words = nltk.corpus.words.words()

# Filter the dictionary to include only 5-letter legible words
five_letter_words = [word for word in words if len(word) == 5 and word.isalpha()]

# Write the words to a text file
with open('5-letter-legible-words.txt', 'w') as file:
    file.write('\n'.join(five_letter_words))

with open('5-letter-legible-words.txt', 'r') as file:
    # Read the contents of the file into a string
    contents = file.read().split()
sign_list=[]
while(True):
    # Print the contents of the file
    guess =input("Enter word:")
    # guess = "ready"
    signs = input("Enter Sign:")

    # signs = "__._X"
    count=0
    point=0
    point_counter=0
    sign_list.append(signs)
    for signs in sign_list:
        print(signs)
    for word in signs:
        if word == "X":
            count+=1
        elif word == ".":
            point_counter+=1
    counter =0
    found=0
    possible = []
    for name in contents:
        for i in range(len(guess)):
                
            if signs[i] == "X" and name[i] == guess[i]:
                counter+=1
            elif signs[i] ==".":
                for j in range(len(name)):
                    if name[j] == guess[i] and j!=i:
                        point+=1
                        break



        if counter == count and point==point_counter:
            consider=0
            possible.append(name)
            
        counter=0
        point=0

    print("Possible words:")
    for name in possible:
        print(name,guess)
    contents=possible





