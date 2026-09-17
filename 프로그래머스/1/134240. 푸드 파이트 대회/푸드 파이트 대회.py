def solution(food):
    answer = ''
    rev_answer = ''
    for i in range(len(food)):
        if i > 0:
            answer += str(i) * (food[i] // 2)
    rev_answer = answer[::-1]
    answer += "0"
    answer += rev_answer
    return answer