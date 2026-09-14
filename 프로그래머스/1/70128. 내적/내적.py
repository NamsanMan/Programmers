def solution(a, b):
    answer = 0
    for i in range(len(a)):
        points = 0
        points = a[i] * b[i]
        answer += points
    return answer