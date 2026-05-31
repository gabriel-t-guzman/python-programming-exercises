from tkinter import filedialog

#filename1 = "ipg2.txt"
#filename2 = "nums.txt"

def selectfile():
    name = filedialog.askopenfilename(title="Choose file")
    return name
    

t_bloco = 1024
def comparefiles (filename1, filename2):
    with open(filename1, "rb") as file1, open(filename2, "rb") as file2:
        while True:
            bloco1 = file1.read(t_bloco)
            bloco2 = file2.read(t_bloco)

            if bloco1 != bloco2 :
                print("Son diferentes!")
                return
            if not bloco1 : break
        print("Son iguales!")

def main():
    f1 = selectfile()
    f2 = selectfile()
    comparefiles(f1, f2)

main()
#comparefiles(filename1, filename2)
   
        

