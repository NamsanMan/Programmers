def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_all(arr):
    g = arr[0]
    for x in arr[1:]:
        g = gcd(g, x)
    return g

def all_cd(n):
    i = 1
    arr = []
    while i <= n:
        if n % i == 0 and i != 1:
            arr.append(i)
        i += 1
    return arr

def solution(arrayA, arrayB):
    a = 0
    b = 0
    gcd_A = gcd_all(arrayA)
    gcd_B = gcd_all(arrayB)
    candidates_A = all_cd(gcd_A)
    candidates_B = all_cd(gcd_B)
    while candidates_A:
        num = candidates_A.pop()
        for i in range(len(arrayB)):
            if arrayB[i] % num == 0:
                a = 0
                break
            a = num
        if a == num:
            break
    while candidates_B:
        num = candidates_B.pop()
        for i in range(len(arrayA)):
            if arrayA[i] % num == 0:
                b = 0
                break
            b = num
        if b == num:
            break
    if a == 0 and b == 0:
        return 0
    else:
        return max(a, b)