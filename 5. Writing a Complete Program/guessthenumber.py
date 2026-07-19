# This is a "Guess the Number" Program
import random
print('Hello, human. What is your name?')
yourName = input()
print('Say, ' + yourName + '. I am actually thinking of a number from 1 to 20.')
secretNumber = random.randint(1, 20)

# Guessing Game Loop
try:
    for numGuess in range(1, 7):
        print('Take a guess')
        guessTaken = int(input())
        if guessTaken > 20:
            print('You are not taking this seriously. I am done. >:(')
            break
        elif guessTaken < 1:
            print('You are not taking this seriously. I am done. >:(')
            break
        elif guessTaken > secretNumber:
            print('Lower.')
        elif guessTaken < secretNumber:
            print('Higher.')
        elif guessTaken == secretNumber:
            print('You got it, ' + yourName + '! The number is ' + str(secretNumber) + '. :)')
            break
        else:
            print('You are not taking this seriously. I am done. >:(')
            break
    else:
        print('I lost patience. You have already guessed ' + str(numGuess) + ' times! The number is ' + str(secretNumber) + '. :(')
except ValueError:
    print('You did not select a valid number! >:(')
