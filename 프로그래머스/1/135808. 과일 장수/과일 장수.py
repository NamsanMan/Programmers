def solution(k, m, score):
    answer = 0
    ascend_score = sorted(score, reverse = True)
    
    for i in range(0, len(ascend_score) - m + 1, m):
        answer += ascend_score[i + m - 1] * m
    

    return answer