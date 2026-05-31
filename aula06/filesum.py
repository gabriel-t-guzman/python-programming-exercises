from tkinter import filedialog

def main():
    # 1) Pedir nome do ficheiro (experimente cada alternativa):
    #name = input("File? ")                                  #A
    name = filedialog.askopenfilename(title="Choose File") #B
    
    # 2) Calcular soma dos números no ficheiro:
    total = fileSum(name)
    
    # 3) Mostrar a soma:
    print("Sum:", total)


def fileSum(filename):
    # Complete a função para ler números do ficheiro e devolver a sua soma.
    a = 0
    s = 0
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            print(line)
            line = float(line)
            s += line     
    return s


if __name__ == "__main__":
    main()

