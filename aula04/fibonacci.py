# fibonnaci function F(n) = F(n-1) + F(n-1) , n>1  F(0)=1 & F(1)=1
'''
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else :
        return fibonacci(n-1)+fibonacci(n-2)

'''



lista = [0, 1]
def fibo(x):
    A1 = 0
    A2 = 1
    for i in range (3,x+1):
        An = A1 + A2
        A1 = A2
        A2 = An
        lista.append(An)
    return lista



n = int(input("termo? "))

print(fibo(n))

