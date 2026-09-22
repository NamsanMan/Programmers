def solution(N, stages):
    answer = []
    temp = []

    for i in range(1, N + 1):
        son = 0
        mother = 0

        for j in range(len(stages)):
            if i == stages[j]:
                son += 1

            if i <= stages[j]:
                mother += 1

        if mother == 0:
            temp.append((i, 0))
        else:
            temp.append((i, son / mother))

    temp = sorted(temp, reverse=True, key=lambda x: x[1])

    for i in range(len(temp)):
        answer.append(temp[i][0])

    return answer