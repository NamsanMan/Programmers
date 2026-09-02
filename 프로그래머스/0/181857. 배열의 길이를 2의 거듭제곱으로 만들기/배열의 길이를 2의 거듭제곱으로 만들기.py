def solution(arr):
    answer = arr
    target = 1

    while target < len(answer):
        target *= 2

    while len(answer) < target:
        answer.append(0)

    return answer