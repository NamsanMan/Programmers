def solution(n, words):
    answer = []
    break_flag = False
    for i in range(1, len(words)):
        if len(words[0]) == 1:
            answer = [1, 1]
            break
        elif len(words[i]) == 1:
            answer = [i % n + 1, i // n + 1]
            break
        elif words[i - 1][-1] != words[i][0]:
            answer = [i % n + 1, i // n + 1]
            break
        for j in range(0, i):
            if words[j] == words[i]:
                answer = [i % n + 1, i // n + 1]
                break_flag = True
                break
        if break_flag == True:
            break
    if answer == []:
        return [0, 0]
    else:
        return answer