def print_n_1(n):
    if n<=0:
        return
    #print_n_1(n-1) # Back Tracking
    print(n)
    print_n_1(n-1)

n=int(input("Enter n: "))
print_n_1(n)