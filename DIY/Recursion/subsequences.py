def printF(i, temp, arr, n):
    if i == n:
        print(temp)
        return

    temp.append(arr[i])
    printF(i+1, temp, arr, n)
    temp.remove(arr[i])
    printF(i+1, temp, arr, n)

arr = [3,1,2,0]
printF(0, [], arr, len(arr))

# Time Complexity: O(2**n)
# Space Complexity: O(n)