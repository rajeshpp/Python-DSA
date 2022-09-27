def dec_to_bin(n):
    assert int(n) == n, "Please enter an integer value."
    if n == 0:
        return 0
    if n<0:
        n =  -1*n
    return n%2 + 10 * dec_to_bin(n//2)


print(dec_to_bin(109))