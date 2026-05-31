def ispalindrome(s):
    ns = s[::-1]
    print (ns)
    if s == ns : return True
    return False

a = ispalindrome('arepera')
d = ispalindrome('foof')
print (a)
print (d)

