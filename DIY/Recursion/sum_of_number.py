def sum_of_number(n):
    if n<0:
        return ("Please enter positive integer number.")
    if all((n>=0, n<10)):
        return n
    return n%10+sum_of_number(n//10)

print(sum_of_number(int(input("Enter a Number: "))))