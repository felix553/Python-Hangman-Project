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
    global word
    global length
    global strike
    global guesses
    global display
    global already_guessed
    global game_over
    game_over = 1
    word = choose_words()
    length = len(word)
    strike = 8
    guesses = 0
    display = '_' * length
    already_guessed = []

def play_again():
    start = input("Hit Enter to keep playing, or Hit 'q' to quit \n")
    while(start):
        if start == "e":
            initialise_game()
            hangman()
            break
        elif start == "q":
            print("\nThe game will now end")
            print("\nThanks for playing!")
            break
        else:
            start = input("\nHit Enter to keep playing, or Hit 'q' to quit")

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def hangman():
    global word
    global length
    global strike
    global guesses
    global display
    global already_guessed
    global game_over
    print("\nThe Game Will Now Begin, Good Luck " + name + "!\n")
    while (strike > 1):
        print("Strikes: " + str(strike - 1) + "   Guesses: " + str(guesses))
        print ("Already Guessed Characters: " + str(already_guessed))
        print(display + "\n")
        guess = input("Please enter your guess: ").upper()
        while (guess):
            if guess in already_guessed:
                guess = input("\nYou already guessed " + guess + ", guess another character: ")
            elif guess in word:
                print("\nYou guessed right!\n")
                new_display = ""
                for char, char2 in zip(word, display):
                    if char == guess:
                        new_display += char
                    elif char2 != '_':
                        new_display += char2
                    else: 
                        new_display+= '_'
                display = new_display
                break


            else:
                print("\nYou guessed wrong!\n")
                strike -= 1
                print(HANGMANPICS[-int(strike)] + '\n')
                break

        already_guessed.append(guess)
        guesses += 1
        if word == display:
            print("Congratulations! You have guessed the word: " + word + " in " + str(guesses) + " guesses\n")
            game_over = 0
            break
    if game_over:
        print("Game Over! You have run out of guesses!\n")
    
    play_again()


    return 

def choose_words():
    global word
    word = input("\nEnter word to guess: ")
    while(word): 
        if len(word) >= 3:
            return word.upper()
        else:
            word = input("\nPlease enter longer word: ")

main()


    
    


