import time 

# Introduction to Hangman game 

print("\nWelcome to the Hangman game!\n")
name = input("Enter your name: ")
print("\nGood Luck " + name + "!\n")
time.sleep(1.5)

start = input("Hit Enter to start playing, or Hit 'q' to quit \n")
while(start):
    if start == "e":
        print("\nThe game will now begin. Have Fun!")
        break
    elif start == "q":
        print("\nThe game will now end")
        break
    else:
        start = input("\nHit Enter to start playing, or Hit 'q' to quit")


def main():

    initialise_game()
    hangman()
    

def initialise_game():
    global strike 
    global guesses
    global display
    global word
    global already_guessed
    global length

    word = choose_words()
    length = len(word)
    strike = int(length/2)
    guesses = 0
    display = '_' * length
    already_guessed = []

def play_again():
    return

def hangman():
    print("\nThe Game Will Now Begin, Good Luck " + name + "!")
    return 

def choose_words():
    word = input("\nEnter word to guess: ")
    while(word): 
        if len(word) >= 3:
            return word
        else:
            word = input("\nPlease enter longer word: ")

main()


    
    


