import random

def welcome():
    print("Welcome! Are you ready to play hangman? (Y/N)")
    return input()
        
def guess_word():
    while True:

        alreadyGuessed = correctGuess + wrongGuess

        print("Guess a letter")
        letter = input()
        letter = letter.lower()
        if len(letter) != 1:
            print("Enter a single letter")
        elif letter not in 'abcdefghijklmnopqrstuvwxyz':
            print("Enter a LETTER!!")
        elif letter in alreadyGuessed:
            print("You've already guessed the letter.")
        else:
            return letter

def display():
    print("Wrong Guesses : ", end = '')
    for i in wrongGuess:
        print(i, end = '')
    print()

    blank  = "_" * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctGuess:
            blank = blank[:i] + secretWord[i] + blank[i+1:]
        
    for i in blank:
        print(i, end = '')
    print()    

if __name__ == "__main__":

    secretWord = "python"
    correctGuess = ''
    wrongGuess = ''
    count = 7


    choice = welcome()
    if choice == 'Y' or 'y':
        while True:
            display()

            guess = guess_word()
            if guess in secretWord:
                correctGuess = correctGuess + guess

                foundAll = True
                for i in range(len(secretWord)):
                    if secretWord[i] not in correctGuess:
                        foundAll = False
                        break
                if foundAll:
                    print("YAY!! You won!!")
                    exit()
            else:
                wrongGuess = wrongGuess + guess

                if len(wrongGuess) == count:
                    display()
                    print("You have run out of guesses!")
                    print("The correct word is "+ secretWord)
                    exit()

    else:
        exit()
