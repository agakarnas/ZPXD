import sys 
import random

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' %(wins, losses, ties))
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        yourMove = input()
        if yourMove == 'q':
            sys.exit()
        if yourMove == 'r' or yourMove == 'p' or yourMove == 's':
            break
        print('Type one of r, p, s or q.')
    
    if yourMove == 'r':
        print('Rock vs. ...')
    elif yourMove == 'p':
        print('Paper vs ...')
    elif yourMove == 's':
        print('Scissors vs. ...')
    
    RandNum = random.randint(1,3)

    if RandNum == 1:
        computermove = 'r'
        print('Rock')
    elif RandNum == 2:
        compMove = 'p'
        print('Paper')
    elif RandNum == 3:
        compMove = 's'
        print('Scissors')
    
    if yourMove == compMove:
        print("It's a tie!")
        ties = ties + 1
    
    elif yourMove == 'r' and compMove == 's':
        print('You won!')
        wins = wins + 1
    
    elif yourMove == 's' and compMove == 'p':
         print('You won!')
         wins = wins + 1   
         
    elif yourMove == 'p' and compMove == 'r':
        print('You won!')
        wins = wins + 1
    
    elif yourMove == 'p' and compMove == 's':
        print('You lost!')
        losses = losses + 1

    elif yourMove == 's' and compMove == 'r':
        print('You lost!')
        losses = losses + 1
    
    elif yourMove == 'r' and compMove == 'p':
        print('You lost!')
        losses = losses + 1
