def solution(num):
    answer = 0
    x = num
    if x == 1:
        return 0
    while 1:
        if x == 1:
            return answer
        if x % 2 == 0:
            x = x / 2
            answer += 1
        elif x % 2 == 1:
            x = x * 3 + 1
            answer += 1
        if answer >= 500:
            return -1 