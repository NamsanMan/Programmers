def solution(n):
    answer = []
    trail = 0
    for i in range(1, n + 1):
        if i == n:
            for l in range(n, 2 * n):
                answer.append(l)
        else:
            for j in range(i):
                if j == 0:
                    answer.append(i)
                else:
                    answer.append(0)
    trail += 2
    number = answer[-1]
    while trail < n + 1:
        zero_flag = False
        if trail % 3 == 2:
            for i in range(len(answer) - 1, 0, -1):
                if zero_flag == False and answer[i] == 0:
                    number += 1
                    answer[i] = number
                    zero_flag = True
                elif zero_flag == True and answer[i] != 0:
                    zero_flag = False
            trail += 1
        elif trail % 3 == 0:
            for i in range(len(answer)):
                if zero_flag == False and answer[i] == 0:
                    number += 1
                    answer[i] = number
                    zero_flag = True
                elif zero_flag == True and answer[i] != 0:
                    zero_flag = False
            trail += 1
        elif trail % 3 == 1:
            for i in range(len(answer)):
                if answer[i] == n - trail // 3:
                    start_idx = i
                    break
            for i in range(start_idx + trail // 3 + 1, len(answer)):
                if answer[i] == 0:
                    number += 1
                    answer[i] = number
                else:
                    break
            trail += 1
    
    return answer