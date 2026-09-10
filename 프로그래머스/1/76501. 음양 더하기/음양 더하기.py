def solution(absolutes, signs):
    answer = 0
    a = 0
    
    for i in range(len(signs)):
        if signs[i]:
            a = 1
        else:
            a = -1
        answer += absolutes[i] * a
    return answer