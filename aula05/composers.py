# jmr 2024 o programa

import sys
from dates5 import *
# Add auxiliary functions here.



def load_lifetimes_file(file_name):
    """Load birth, death, name data from a file."""
    lst = []
    with open(file_name, 'r') as file:
        for line in file:
            # Strip spaces and newline from line
            line = line.strip()
            # Ignore empty lines and comments
            if line == "" or line[:1] == "#":
                continue  # skip to next line
            # Change this to split the line, parse dates
            line = line.split("\t")
            # and store (date1, date2, name) tuple.
            line[0] = parseMDY(line[0])
            line[1] = parseMDY(line[1])
            ...
            lst.append(line)
    return lst


def main():
    file_name = 'composers.txt'  # Replace with your file name
    lifes = load_lifetimes_file(file_name)

    print("THE DEAD COMPOSERS SOCIETY")
    print("==========================")
    
    for info in lifes:
        # Change this to show Name, Age and Date-of-death in aligned columns.
        b = str(info[1]) 
        a = str(info[0])
        if info[0][0] >= 1801 and info[0][0] <= 1900 : print(f"{a:<15}    |    {b:<15}    |    {info[2]:<45}")

        
    print((len(lifes)))

if __name__ == "__main__":
    main()

