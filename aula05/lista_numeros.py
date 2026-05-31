vd = True
Lista = [] # definition of the pricipal variable, what is a list
def inputFloatlist (): # def that creates a list with numbers, and stops when an '' is inserted
    while True :
        digito = input('digitos de la lista?')
        if digito == '' : break
        digito = float(digito)
        Lista.append(digito)
    return Lista # return a 'list'
 
def countLower (Lista,v): # def that counts in the list the amount of numbers smallers than 'v'
    if  Lista == [] : return
    n = 0
    v = int(input('v?'))
    for i in Lista:
        if v > i: n += 1
    return print(n) # return a 'int' 

def minmax (Lista): # Use any list
   
    if Lista == []  : return
    a = 0 # variable that will be the max number of the list
    if len(Lista) == 1 : return (Lista[0]) # if the list is 1-value, is the max and min
    b = Lista [1] # variable that will be the min number of the list
    for i in Lista: # Finding the max whitout 'max'
        if i > a: a = i #find max
        if i < b: b = i # find min
    return a,b      #return a tuple

def media (): 
    if Lista == [] : return
    a = 0
    count = 0
    for i in Lista:
        a += i
        count += 1
    media_de_lista = a/count
    return media_de_lista
 
def main (): 

    inputFloatlist()
    # print the generated list
    print ((minmax(Lista))) #debugin
    print (media ()) # debugin
    countLower (Lista,media())
main () 
