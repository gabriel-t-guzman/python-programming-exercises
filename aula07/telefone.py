# Complete este programa como pedido no guião da aula.

def addcontacts(dic):
    num = str(input("numero? "))
    nome = str(input("nome? "))
    if num in dic : return print(f"Ja esta ca! o num {num} e de {dic[num]}")
    dic[num] = nome

def rmcontact(dic):
    num = str(input("numero? "))
    if num not in dic : return print(f"Nao esta ca! o num {num}")
    del dic[num]

def procurar(dic):
    num = str(input("numero? : "))
    a = dic.get(num, num)
    print(a)

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {:^25s} : {:<12s}".format("Numero", "Nome", "Morada"))
    for num in dic:
        if type(dic[num]) is tuple : print("{:>12s} : {:^25s} : {:<12s}".format(num, dic[num][0], dic[num][1]))
        if type(dic[num]) is not tuple :print("{:>12s} : {:^25s} : {:<12s}".format(num, dic[num], "None"))

def filterPartName(c, partName):
    """Returns a new dict with the contacts whose names contain partName."""
    new_dc = {}
    num = len(partName)
    for i in c:
        if c[i][:num] == partName: 
            new_dc.setdefault(c[i], i)
    print (new_dc)

def morada(contatos):
    num = str(input("Numero : "))
    mor = str(input("Direcao? : "))

    

def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    print("Adicionar (M)orada")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": ("Universidade de Aveiro", "Santiago, Aveiro"),
        "727392822": ("Cristiano Aveiro", "Porto"),
        "387719992": ("Maria Matos", "Coimbra"),
        "887555987": "Marta Maia",
        "876111333": "Carlos Martins",
        "111222333": "Ana Bacalhau"
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op == "A":
            addcontacts(contactos)
        elif op == "R":
            rmcontact(contactos)
        elif op == "N":
            procurar(contactos)
        elif op == "P":
            filterPartName(contactos, input("nome:"))
        elif op == "M":
            morada(contactos)
        else:
            print("Não implementado!")
    

# O programa começa aqui
main()

