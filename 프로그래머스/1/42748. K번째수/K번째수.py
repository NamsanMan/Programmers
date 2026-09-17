def solution(array, commands):
    answer = []
    temp = []
    for i in range(len(commands)):
        temp = array[commands[i][0] - 1 : commands[i][1]]
        temp = sorted(temp)
        answer.append(temp[commands[i][2] - 1])
        temp = []
    return answer