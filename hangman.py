import random


#open file to read a random word
with open("words.txt", "r") as file:
    words = file.read().split()

#Choose a random word
secret_word = words[random.randint(0, len(words)-1)]

#initialize varaibles
Max_guesses = 6
guess_list=["_"]*(len(secret_word))


#used to take the guess list, a guess, the secret woprd and updating the characters
def update_list(secret_word, guess, guess_list):
    for i, letter in enumerate(secret_word):
        if letter == guess:
            guess_list[i] = guess
    return guess_list


while Max_guesses > 0:
    #ask for user input
    if "_" not in guess_list:
        print("Great job, you did it: the word was: ", secret_word)
        break

    print("remaining lives: ", Max_guesses)
    print(secret_word)
    print("guess the letters in: ", guess_list, "what is your guess")
   
    guess = input().lower()

    #check if input is alphanumeric and is in secret word list
    if guess in guess_list:
        print("You already guessed that letter.")
        continue 
    if (guess.isalpha() and guess in secret_word) and len(guess)==1:
        print("good guess")
        #update the guess list
        guess_list = update_list(secret_word, guess, guess_list)
    elif len(guess)>2:
        print("cannot guess 2 words")
    elif (guess not in secret_word):
        print("wrong Guess")
        Max_guesses -=1
    else:
         print("wrong Type of answer")
    


#end of game
print("game over, answer was: ", secret_word)
    
        
    