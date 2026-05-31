"""
This program generates 20 terms of a sequence by a recurrence relation.
Change it to show all positive terms of the sequence and count them.
Format the columns to make the output look like this:
   n        Un
   0   100.000
   1    99.990
   2    99.980
"""

'''
for n in range(20):
    print(n, Un)
    Un = Un-1
    Un = 1.01*Un - 1.01     # Set Un to the next term of the sequence
'''

n = int(input('Quantos termos queres? '))
print("n", "Un")
contador = 0
Un = 100

for i in range (n+1) :

    print (f'{i} {Un:.3f}')
    Un = 1.01*( Un - 1)

print (f'Foram contados {i} termos')

