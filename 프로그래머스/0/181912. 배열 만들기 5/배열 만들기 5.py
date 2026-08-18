def solution(intStrs, k, s, l):
    answer = []
    for x in intStrs:
        i = int(x[s:s+l])
        if i > k:
            answer.append(i)
            
    return answer