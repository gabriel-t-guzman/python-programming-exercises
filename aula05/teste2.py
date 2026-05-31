'''
def factorial (n):
    a = 1
    print (n, end="! = ")
    for i in range (n,0,-1):
        a *= i
        if i != 1 : print (i, end=" x ")
    print (i, end=" = ")
    print (a)
    return a
'''
def factorial(n):
    a = 1
    text2 = ''
    for i in range (n,0,-1):
        a *= i
        text2 += str(i) + ' x '
    text1 = str(n) + '! = '
    text3 = '= ' + str(a)
    text = text1 + text2 + text3
    return text



x = int(input('n?'))
s = factorial(x)
print (s)

# print (factorial(x))
