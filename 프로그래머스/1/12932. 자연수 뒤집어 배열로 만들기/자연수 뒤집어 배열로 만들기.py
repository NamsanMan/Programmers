def solution(n):
    answer = []
    str_n = str(n)
    str_n = str_n[::-1]
    for i in str_n:
        answer.append(int(i))
    return answer