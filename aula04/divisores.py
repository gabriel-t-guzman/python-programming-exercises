#def tipo_de_n ()
Divisores = []

n = int(input('n?'))

def tipo_de_n(lista_div):
    s = sum (lista_div)
    tipo = ''
    if s < n:
        tipo = 'deficiente'
    elif s > n:
        tipo = 'abundate'
    else:
        tipo = 'perfeito'
    return tipo

def divisores (n):
    for i in range (1,n):
        if n%i == 0:
            Divisores.append(i)
    print (tipo_de_n(Divisores))
    return Divisores

print (divisores(n))

