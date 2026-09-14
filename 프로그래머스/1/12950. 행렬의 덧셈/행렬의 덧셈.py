def solution(arr1, arr2):
    answer = []
    for a in range(len(arr1)):
        row = []
        for b in range(len(arr1[a])):
            row.append(arr1[a][b] + arr2[a][b])
        answer.append(row)
    return answer