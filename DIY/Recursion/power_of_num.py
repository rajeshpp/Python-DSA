def power_of_num(m,n):
    assert m>=0 and n>=0 and int(n) == n and int(m) == m, "m and n should be positive integers only."
    if n==0:
        return 1
    return m*power_of_num(m, n-1)

print(power_of_num(10,2))