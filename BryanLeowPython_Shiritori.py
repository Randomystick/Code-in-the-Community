#Shiritori.py
#Problem Specifications: https://imgur.com/a/AIyAtdP


hash_table = [[] for _ in range(26)] 
    #declare a hash table data structure to insert the words in alphabetical order
    #26 keys available, one for each alphabet (a,b,c,...)
    #implemented as a nested list (Python in-built data structure) to prevent collision 
    #i.e. to allow one key to map to multiple values (a = apple, air,...)


with open("word_list.txt") as openfileobject:
    for line in openfileobject: #for every word in the word list 
        wordBuffer = line.lower() #convert to smallcaps
        wordBuffer = wordBuffer.strip() #remove the newline character \n
        hashKey = ord(wordBuffer[0]) - 97 #extract first letter of word, convert to intenger (a = 0, b = 1, c = 2 etc), store in hashKey
        hash_table[hashKey].append(wordBuffer) #hash word into hash table
#DEBUG print("Words starting with z are the following:", hash_table[25])
#DEBUG print("There are", len(hash_table[25]), "z words in total")

gameOver = 0 #boolean to check if one of three cases have been violated
    #Case 1: You didn't type a word starting with ' '
    #Case 2: You typed a word that has been typed before.
    #Case 3: You didn't type a word found in word_list.txt


def checkWord(wordTyped, hash_table): #function to check if word exists in word_list
    wordTypedKey = ord(wordTyped[0]) - 97 #same concept as hashKey
    for _ in range(len(hash_table[wordTypedKey])): #_ is just an unused variable for the loop
        if wordTyped in hash_table[wordTypedKey]:
            return 0 #for gameOver
        else:
            print("You didn't type a word found in word_list.txt")
            return 1 #for gameOver


#GAME START
#First game loop only needs to check for Case 3
print("Please type a word: ", end="")
wordTyped = input()
words_typed_so_far = [wordTyped] #initialise the list of typed words (not hashed since it won't be very big)
wordLastofPrevious = wordTyped[-1]
gameOver = checkWord(wordTyped, hash_table)


#MAIN GAME LOOP
while not gameOver:
    print("Please type a word: ", end="")
    wordTyped = input()

    #Case 1: You didn't type a word starting with ' '
    if wordTyped[0] == wordLastofPrevious: #the word is correct
        wordLastofPrevious = wordTyped[-1]
    else:
        print("You didn't type a word starting with '", wordLastofPrevious, "'", sep='')
        gameOver = 1
        break #ensure only one error prints

    #Case 2: You typed a word that has been typed before.
    if wordTyped not in words_typed_so_far:
        words_typed_so_far.append(wordTyped)
    else:
        print("You typed a word that has been typed before")
        gameOver = 1
        break

    #Case 3: You didn't type a word found in word_list.txt
    gameOver = checkWord(wordTyped, hash_table)