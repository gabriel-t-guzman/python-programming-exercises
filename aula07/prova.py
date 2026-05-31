a = {'1':'A', '2':'B'}
l = []

for i in a:
    t = (i,a[i])
    l.append(t)

print(l)

b = a.items()
print(b)

