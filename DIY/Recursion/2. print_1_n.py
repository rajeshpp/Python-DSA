def print_1_to_n(i):
    if i>n:
        return
    
    #print_1_to_n(i+1) # Back Tracking
    print(i)
    print_1_to_n(i+1)

n=int(input("Enter n: "))
print_1_to_n(1)