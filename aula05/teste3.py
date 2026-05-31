s = 'john@ua.pt'
c = 'jo..@ua.pt'
f = 'ap'
p = 'cdia@ua..pt'
k = 'dsa%@ua.pt'

msgf = 'Errorf'
msgu = 'Erroru'
msgd = 'Errord'
msg = 'Valid'

def verificar(email):
    if '@' not in email : return msgf 
    if len(email) < 3 : return msgf
    lista_s = email.split('@')
    #verificar user
    a = lista_s[0]
    if len(a) < 3 : return msgu
    for i in a:
        if i.isalpha() == False and i.isdigit() == False and i != '.' : return msgu 
    for i in range(len(a)):
        if a[i] == '.':
            if a[i] == a[i-1]: return msgu
    #verificar dominio
    b = lista_s[1]
    if len(b) < 3 : return msgd
    for i in b:
        if i.isalpha() == False and i.isdigit() == False and i != '.' : return msgd 
    for i in range(1,len(b)):
        if b[i] == '.':
            if b[i] == b[i-1]: return msgd
    return msg

print (verificar(s))
print (verificar(c))
print (verificar(f))
print (verificar(p))
print (verificar(k))
