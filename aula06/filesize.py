import os 

#def selectdir():
 #   name = filedialog.askopenfilename(title="Choose file")
  #  return name

dire = "/home/getar/Documents/FP/aula06"

def countsize(name):
    file_list = os.listdir(name)
    for file in (file_list):
        size = os.stat(file).st_size
        print (file, size)


def main():
    countsize(dire)

main()
