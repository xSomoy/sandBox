secretWord = "giraffe"
guess = ""
guessCount = 0
guessLimit = 3
outOfGuess = False

while guess != secretWord and not(outOfGuess):
    if  guessCount < guessLimit:
        guess = input("Enter Guess:")
        guessCount += 1
    else:
        outOfGuess = True
if outOfGuess:
    print("Out Of Guesses, You Lose")
else:
    print("You Win!")