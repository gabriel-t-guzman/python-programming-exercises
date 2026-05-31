
def primesUpTo(n):
    s = {i for i in range(2,n+1)}
    for i in range(2, int(n**0.5)+1):
        if i in s : s -= {i*j for j in range(i,(n//i)+1)}
    return (s)

    

def main():
    # Testing:
    s = primesUpTo(1000)
    print(s)

    # Do some checks:
    assert primesUpTo(30) == {2,3,5,7,11,13,17,19,23,29}
    assert len(primesUpTo(1000)) == 168
    assert len(primesUpTo(7918)) == 999
    assert len(primesUpTo(7919)) == 1000
    print("All tests passed!")

if __name__ == "__main__":
    main()

