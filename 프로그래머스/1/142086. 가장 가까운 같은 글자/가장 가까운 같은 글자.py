def solution(s):
    answer = []
    answer.append(-1)
    for i in range(len(s)):
        if i != 0:
            max_j = -1
            for j in range(0, i):
                if s[i] == s[j]:
                    max_j = j
            if max_j == -1:
                answer.append(-1)
            else:
                answer.append(i - max_j)
    return answer