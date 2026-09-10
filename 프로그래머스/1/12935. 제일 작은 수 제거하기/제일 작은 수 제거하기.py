def solution(arr):
    answer = arr[:]
    small = min(arr)

    if not len(arr) == 1:
        answer.remove(small)
        return answer
    else:
        return [-1]