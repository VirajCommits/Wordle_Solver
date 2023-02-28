guess = "break"
with open('5-letter-legible-words.txt', 'r') as file:
    # Read the contents of the file into a string
    contents = file.read().split()
for i in range(len(contents)):
    contents[i]=contents[i].lower()
pos=0
all_dashes = ['b','r','e','a','k']
for letter in all_dashes:
    while(pos<len(contents)):
        name = contents[pos]
        if letter in name:
            contents.remove(name)
        else:
            pos+=1
    pos=0
print(contents)