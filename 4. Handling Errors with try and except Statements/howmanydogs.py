print('How many doggos do you have?')
numDoggos = input()
try:
    if int(numDoggos) >= 4:
        print('That is a lot of good doggos :)')
    elif int(numDoggos) < 0:
        print('You thought I would not catch your trickery, hmm?')
    else:
        print('Awww. You need to add more :(')
except ValueError:
    print('You did not input a number >:(')
