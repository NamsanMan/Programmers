def solution(d, budget):
    answer = 0
    sorted_d = sorted(d)
    summation = 0

    for i in range(len(sorted_d)):
        if summation + sorted_d[i] <= budget:
            answer += 1
            summation += sorted_d[i]
        else:
            return answer

    return answer