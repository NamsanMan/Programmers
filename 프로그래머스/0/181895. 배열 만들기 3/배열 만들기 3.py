def solution(arr, intervals):
    answer = []
    for i in intervals:
        for a in range(i[0], i[1] + 1):
            answer.append(arr[a])
    return answer