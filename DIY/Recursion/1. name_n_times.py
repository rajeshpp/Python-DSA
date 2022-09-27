def print_name(n):
    if n<=0:
        return
    print('Rajesh')
    n-=1
    print_name(n)

n=int(input("Enter n:"))
print_name(n)