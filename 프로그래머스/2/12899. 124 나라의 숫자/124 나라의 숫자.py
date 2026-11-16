def solution(n):
    answer = ''
    while n > 0:
        record = n % 3
        n = n // 3
        if record == 0:
            answer += '4'
            n = n - 1
        elif record == 1:
            answer += '1'
        elif record == 2:
            answer += '2'
    return answer[::-1]