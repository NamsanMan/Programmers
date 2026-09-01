def solution(arr1, arr2):
    if len(arr1) > len(arr2):
        return 1
    elif len(arr1) < len(arr2):
        return -1
    
    sum1 = 0
    sum2 = 0

    for a in arr1:
        sum1 += a

    for b in arr2:
        sum2 += b

    if sum1 > sum2:
        return 1
    elif sum1 < sum2:
        return -1
    else:
        return 0