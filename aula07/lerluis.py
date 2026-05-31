from tkinter import filedialog

def selectfile():
    name = filedialog.askopenfilename()
    return name


def countletters(nomefile):
    with open(nomefile, "r") as file:
        d = {}

        for line in file:
            for i in line:
                if i.isalpha(): 
                    i = i.lower()
                    d.setdefault(i, 0)
                    d[i] += 1
        d = dict(sorted(d.items(), key= lambda i:i[1], reverse=True ))
        return d 
   
def main():
    a = selectfile()
    b = countletters(a)
    for i in b:
        print (i, b[i])

main()
