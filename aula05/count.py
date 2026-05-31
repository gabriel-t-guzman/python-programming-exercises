def count (frase) :
    a = 0
    for i in frase:
        if i.isdigit():
            a += 1
    return a

