def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def lcm(a, b):
    return a * b // gcd(a, b)

def solution(arr):
    numbers = arr[:]
    answer = numbers[0]
    
    for i in range(1, len(numbers)):
        answer = lcm(answer, numbers[i])
    
    return answer