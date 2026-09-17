def solution(strings, n):
    answer = []

    for word in strings:
        answer.append(word[n] + word)

    answer.sort()

    for i in range(len(answer)):
        answer[i] = answer[i][1:]

    return answer