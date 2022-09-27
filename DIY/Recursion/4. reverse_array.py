import time
# Solution 1
t1=time.time()
a = [2,45,34,435,2,53453,43,5]
i=0
j=len(a)-1
print("Original Array: ", a)
while i<j:
    a[i], a[j] = a[j], a[i]
    i+=1
    j-=1

print("Reversed Array: ", a)
t2=time.time()
print("Time taken for Solution 1: ", t2-t1)

# Solution 2 - Won't support if limit crosses maximum recursion depth
t1=time.time()
a = [2,45,34,435,2,53453,43,5]
i=0
j=len(a)-1
print("Original Array: ", a)
def reverse_arr(i,j):
    if i>=j:
        return
    a[i], a[j] = a[j], a[i]
    reverse_arr(i+1,j-1)

reverse_arr(i,j)

print("Reversed Array: ", a)
t2=time.time()
print("Time taken for Solution 2: ", t2-t1)


# Solution 3
t1=time.time()
a = [2,45,34,435,2,53453,43,5]
i=0
n=len(a)
print("Original Array: ", a)
def reverse_arr(i):
    if i >= n-i-1:
        return
    a[i], a[n-i-1] = a[n-i-1], a[i]
    reverse_arr(i+1)

reverse_arr(i)

print("Reversed Array: ", a)
t2=time.time()
print("Time taken for Solution 3: ", t2-t1)