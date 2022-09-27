n=int(input("Enter a Number: "))
cnt=0
def fib(n):
    global cnt # Usage of global is not a good practice
    cnt+=1
    if n<=1:
        return n
    elem = fib(n-1)+fib(n-2)
    return elem

print(fib(n),'is the fibonacci number for n:',n)
print(cnt, 'recursion calls made for n:', n)