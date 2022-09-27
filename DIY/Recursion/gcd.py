def gcd(m,n):
    assert int(m) == m and int(n) == n, "m and n should be integeres only."
    if m<0:
        m = -1 * m
    if n<0:
        n = -1 * n
    if n==0:
        return m
    return gcd(n, m%n)


print(gcd(18,48))