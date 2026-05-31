#n = int(input('n?')
def isPrime ():
    for i in range (2,21):
        is_prime = True
        for j in range (2,i):
            if i%j == 0:
                is_prime = False
                break 
        if is_prime :
            print(i,'is True-------')
        else :
            print (i,'is False')

print (isPrime())
