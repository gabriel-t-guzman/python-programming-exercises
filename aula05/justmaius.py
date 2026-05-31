def abreviar(postr):
    abreviado = ''
    for i in postr:
        if i.isupper() == True : abreviado += i
    return abreviado


a = abreviar('Universidade de Aveiro')
print (a)


