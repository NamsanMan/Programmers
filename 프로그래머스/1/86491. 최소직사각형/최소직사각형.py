def solution(sizes):
    answer = 0
    temp = []
    w_max = 0
    h_max = 0

    for i in range(len(sizes)):
        temp.append(sorted(sizes[i]))

    for i in range(len(temp)):
        if temp[i][0] > w_max:
            w_max = temp[i][0]

        if temp[i][1] > h_max:
            h_max = temp[i][1]

    answer = w_max * h_max

    return answer