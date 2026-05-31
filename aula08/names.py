file = "names.txt"

def readfile(file):
    with open(file, "r") as file:
        next(file)
        L = []
        while True:
            line = file.readline()
            line = line.strip().split()
            if line == [] : return L
            L.append(line)

def set_value(lst):
    dic = {}
    for n in lst:
        dic.setdefault(n[-1],[]).append(n[0])
    for n in dic:
        dic[n] = set(dic[n])
    return dic


def main():
    lista_nomes = readfile(file)
    fin = set_value(lista_nomes)
    print (fin)

main()
