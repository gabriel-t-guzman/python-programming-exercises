'''
def factorial(n): # numero que entra ex:3
    a = n-1 # definiendo el primer multiplo ex:2
    if n < 0: # no puede tomar valores negativos
        return 'Valor invalido'
    if n > 0: 
        while a > 0: # como ex a:2, se ejecuta
            n*=a # se multiplica 3*2 pero falta *1 
            a-=1 # define el siguiente multiplicador ex:1
        return n ## Finally, n multi por todos los naturales >n, haciendo el factorial
    return 1 # se n==0 el 0! es 1

n = int(input('n?'))
print (factorial(n))
'''

factorial = int(input('n?'))
for i in range (1,factorial):
    factorial *=i
if factorial == 0 : factorial = 1
print (factorial)

