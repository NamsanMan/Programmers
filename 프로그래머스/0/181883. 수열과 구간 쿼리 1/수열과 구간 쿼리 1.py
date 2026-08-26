def solution(arr, queries):
    answer = arr
    for i in range(len(arr)):
        for s, e in queries:
            if s <= i and i <= e:
                answer[i] = answer[i] + 1
    return answer