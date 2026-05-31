# Complete o programa!

# a)
def loadFile(fname, lst):
    with open(fname, "r") as file:
        next(file)
        for line in file:
            line = line.strip().split("\t")
            line[0],line[5],line[6],line[7] = int(line[0]),float(line[5]),float(line[6]),float(line[7])
            line = tuple(line[0:2] + line[5:8]) 
            lst += [line]            
        return lst
            

    
# b) Crie a função notaFinal aqui...
def notaFinal (reg):
    #media = reg[0] + reg[1] + reg[2]
    media =float((reg[2] + reg[3] + reg[4]) /3)
    return media


# c) Crie a função printPauta aqui...
def printPauta(lst,a):
    print(f"{'Numero':>6}{'Nome':^50}{'Nota':>4}", file=a) #cabecalho
    for i in lst :
        A = notaFinal(i)
        print(f"{i[0]:>6}{i[1]:^50}{A:>4.1f}",file=a)
    


# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    
    # ordenar a lista
    lst.sort()
    
    # mostrar a pauta
    fout = open("pauta.txt", "w")
    printPauta(lst,fout)
    fout.close()

# Call main function
if __name__ == "__main__":
    main()


