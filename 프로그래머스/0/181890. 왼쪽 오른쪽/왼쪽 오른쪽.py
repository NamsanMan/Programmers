def solution(str_list):
    answer = []
    x = []
    y = []

    for i in range(len(str_list)):
        if str_list[i] == "l":
            x.append(i)

        if str_list[i] == "r":
            y.append(i)

    # l, r이 모두 없는 경우
    if x == [] and y == []:
        return answer

    # r이 없거나, l이 r보다 먼저 나오는 경우
    if y == [] or (x != [] and min(x) < min(y)):
        return str_list[:min(x)]

    # l이 없거나, r이 l보다 먼저 나오는 경우
    return str_list[min(y) + 1:]