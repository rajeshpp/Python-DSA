def printF(i, s, temp, arr, n):
    if i == n:
        if s == sum:
            print(temp)
        return

    temp.append(arr[i])
    s+=arr[i]
    printF(i+1, s, temp, arr, n)
    temp.remove(arr[i])
    s-=arr[i]
    printF(i+1, s, temp, arr, n)


arr = [1, 2, 1]
sum = 2
printF(0, 0, [], arr, len(arr))