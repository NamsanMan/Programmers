def solution(arr, query):
    answer = arr

    for idx, value in enumerate(query):
        if idx % 2 == 0:
            answer = answer[:value + 1]
        else:
            answer = answer[value:]

    return answer