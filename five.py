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
all_dashes=[]
all_crosses =[]
pos=0
reduce_space=[]
quit=False
while(True):
    # Print the contents of the file
    guess =input("Enter word:")
    if guess == "q":
        quit=True
        break
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

    for i in range(len(signs)):
        if signs[i] == "X":
            all_crosses.append(guess[i])
    
    for i in range(len(signs)):
        
        if signs[i] == "_" and guess[i] not in all_crosses:
            all_dashes.append(guess[i])

    initial = (len(possible))
    for letter in all_dashes:
        while(pos<len(possible)):
            name = possible[pos]
            if letter in name:
                possible.remove(name)
            else:
                pos+=1

    
        pos=0
    all_dashes=[]
    all_crosses=[]

    final=(len(possible))
    reduce_percent = (initial-final)/initial*100
    reduce_percent = round(reduce_percent,2)
    if reduce_percent==100.0:
        break
    print("Possible words:")
    pos=1
    for name in possible:
        print(pos,":",name)
        pos+=1

    contents=possible
    reduce_space.append(reduce_percent)
    print("Reduced Search space by",reduce_percent,"%","(from",initial,"words to",final,"words)")
if quit:
    print("-"*100)
    print("Thanks for using me!!")
    print("-"*100)

else:   
    print("-"*100)
    print("No options available")
    print("-"*100)


for percents in reduce_space:
    print("#"*int(percents/2.0),(percents),"%")






