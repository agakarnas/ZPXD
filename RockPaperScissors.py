import sys 
import random

print('KAMIEŃ, PAPIER, NOŻYCE')

print()
print()

zwyciestwo = 0
porazka = 0
remis = 0

while True:
    print('%s Zwycięstw, %s Porażek, %s Remisów' %(zwyciestwo, porazka, remis))
    print()
    while True:
        print('Co wybierasz: (k)amień, (p)apier, (n)ożyce or (w)yjdź ?')
        TwojRuch = input()
        if TwojRuch == 'w':
            sys.exit()
        if TwojRuch == 'k' or TwojRuch == 'p' or TwojRuch == 'n':
            break
        print()
        print('Wpisz k, p, n lub w.')
        print()
        print()
        
    if TwojRuch == 'k':
        print('Kamień kontra ...')
    elif TwojRuch == 'p':
        print('Papier kontra ...')
    elif TwojRuch == 'n':
        print('Nożyce kontra ...')
    
    RandLiczba = random.randint(1,3)

    if RandLiczba == 1:
        RuchKomputer = 'k'
        print('KAMIEŃ')
    elif RandLiczba == 2:
        RuchKomputer = 'p'
        print('PAPIER')
    elif RandLiczba == 3:
        RuchKomputer = 'n'
        print('NOŻYCE')
    
    if TwojRuch == RuchKomputer:
        print()
        print("Remis!")
        print()
        remis = remis + 1
    
    elif TwojRuch == 'k' and RuchKomputer == 'n':
        print()
        print('Brawo! Zwycięstwo!')
        print()
        zwyciestwo = zwyciestwo + 1
    
    elif TwojRuch == 'n' and RuchKomputer == 'p':
         print() 
         print('Brawo! Zwycięstwo!')
         print()
         zwyciestwo = zwyciestwo + 1   
         
    elif TwojRuch == 'p' and RuchKomputer == 'k':
        print()
        print('Zwycięstwo!')
        print()
        zwyciestwo = zwyciestwo + 1
    
    elif TwojRuch == 'p' and RuchKomputer == 'n':
        print()
        print('Niestety, nie tym razem!')
        print()
        porazka = porazka + 1

    elif TwojRuch == 'n' and RuchKomputer == 'k':
        print()
        print('Niestety, nie tym razem!!')
        print()
        porazka = porazka + 1
    
    elif TwojRuch == 'k' and RuchKomputer == 'p':
        print()
        print('Niestety, nie tym razem!!')
        print()
        porazka = porazka + 1
