import random
secretnumber = random.randint(1,20)
print('i am thinking abt a number between 1 and 20')

for guesstaken in range(1, 7):
    print('Take a guess: ')
    guess = int(input())

    if guess < secretnumber:
        print('ur number is less')
    elif guess > secretnumber:
        print('ur number is high')
    else:
        break
if guess == secretnumber:
    print( 'BINGO!!!  u guessed the number in '+str(guesstaken)+' guesses')
else:
    print('well tried champ, the number in my thoughts was '+ str(secretnumber))