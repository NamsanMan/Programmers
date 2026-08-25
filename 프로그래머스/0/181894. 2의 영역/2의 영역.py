def solution(arr):
    answer = []
    temp = []
    for i in range(len(arr)):
        if arr[i] == 2:
            temp.append(i)
    if temp == []:
        return [-1]
    else:
        for n in range(min(temp), max(temp) + 1):
            answer.append(arr[n])
    return answer