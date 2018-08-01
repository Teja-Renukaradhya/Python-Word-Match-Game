import string
import random
from nltk.corpus import brown

word_list = brown.words() #used from a library
word_set = set(word_list) #used from a library
chance = 1
# Check if word is in set
# "looked" in word_set  # Returns True
# "hurrr" in word_set  # Returns False


list_of_alph = list(string.ascii_lowercase) #list of alphabets from a to z

while True:
    letter_list=random.sample(list_of_alph,4) #Generates valid 4 letters from list_of_alph
    random_word =''.join(letter_list)#Converts list into string and we get a valid word

    if random_word in word_set:
        computer_word = random_word
        break

def logic():
    my_word = input("Enter a 4 letter word :: ")

    e_match = 0
    x_match = 0
    for i in range(len(my_word)):
        if my_word[i] in computer_word:
            if my_word[i]==computer_word[i]:
                x_match+=1
            else:
                e_match+=1
    print("Normal matches are ",str(e_match))
    print("Exact matches are ", str(x_match))
    # print(computer_word)  #Uncomment this if you wanna reveal the word in between the game
    return e_match,x_match

def game():

    chance = 1
    while True:
        print("Chance : ", chance)
        e_match,x_match = logic()


        if chance>10 and e_match!=4:
            print("Sorry you lost the game. The word is ",computer_word)
            exit()
        elif chance<10 and x_match==4:
            print('Awesome, you won the game!')
            exit()
        chance += 1

game()



