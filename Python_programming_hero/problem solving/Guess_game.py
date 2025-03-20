""" get a input from user and guess a random number from 0 to 10.
if user enters right number say him congratulation. otherwise say didn't match.
to stop the process ask to enter q."""


import random
print('To stop anytime, enter: q')
score = 0
while True:
    num = random.randint(0,10)
    guess = input('Guess a number between 0 to 10: ')
    if guess == 'q':
        print('Game Over.')
        break
    try:
        guess_num = int(guess)
    except:
        print('plese use correct input')
        continue
    if guess_num == num:
        print('CONGRATS, you guessed it correctly')
        score = score + 10
        print('your new score: ', score)
    else:
        print('Your guess did not match.')
        print('The number was: ', num)