import math
def primesUpTo(n):
    
    s = {i for i in range(2,n+1)}
    # s = set(range(2,n+1))

    for i in range(2, int(n**0.5)+1):
        if i in s : s -= {i*j for j in range(i,(n//i)+1)}
   
    return(s)



def main():
    print(primesUpTo(120))



main()
