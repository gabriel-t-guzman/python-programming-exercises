# Complete the code to make the HiLo game.

import random
'''
def Encontrar_hilo(secret):
    n = int(input('n?'))
    if secret > n:
        print('Low')
    elif secret < n:
        print ('High')
    else :
        return (print(f'{secret} = {n}'))
    Encontrar_hilo(secret)
'''

def playHiLo():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101);
    print (secret)
    print("I picked a number between 1 and 100. Can you guess it?")
    # put your code here 
   # Encontrar_hilo(secret)
    a = 0
    while secret != a:
        a = int(input('n?'))
        if secret > a:
            print('Low')
        elif secret < a:
            print ('High')
    return print(f'{secret} = {a}')

playHiLo()

