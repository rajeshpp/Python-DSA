def fact_n(n):
    if n<=0:
        return 1
    return n*fact_n(n-1)

print(fact_n(int(input("Enter num: "))))