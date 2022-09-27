# Find max product of 2 elements in the given list
l = [3,4,5,34,34,12,12,23,23,435,23,1,23,72,54]
idx=0

def findMax(l):
    max_elem = l[0]
    for i in range(1,len(l)-1):
        if l[i]>max_elem:
            max_elem = l[i]
            idx = i

    return max_elem,idx

max1 = findMax(l)
del l[max1[1]]
max2 = findMax(l)
print(max1[0]*max2[0])


