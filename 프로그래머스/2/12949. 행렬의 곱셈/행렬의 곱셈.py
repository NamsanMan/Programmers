def solution(arr1, arr2):
    answer = []
    for m in range(len(arr1)):
        row = []
        for p in range(len(arr2[0])):
            summation = 0
            for n in range(len(arr2)):
                summation += arr1[m][n] * arr2[n][p]
            row.append(summation)
        answer.append(row)
        
    print(answer)
    return answer