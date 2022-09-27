
def flatten(arr):
    result = []
    if not arr:
        return []
    for a in arr:
        if isinstance(a, list):
            result.extend(flatten(a))
        else:
            result.append(a)
    return result

for val in [[1, 2, 3, [4, 5]], [1, [2, [3, 4], [[5]]]], [[1], [2], [3]], [[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]]:
    print(flatten(val))