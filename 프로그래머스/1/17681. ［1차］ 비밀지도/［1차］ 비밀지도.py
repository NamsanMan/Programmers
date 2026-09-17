def solution(n, arr1, arr2):
    answer = []

    arr1_bin = []
    arr2_bin = []
    
    for i in range(len(arr1)):
        
        row1 = ''
        while arr1[i] > 0:
            row1 = str(arr1[i] % 2) + row1
            arr1[i] = arr1[i] // 2
        while len(row1) < n:
            row1 = '0' + row1
        arr1_bin.append(row1)
        
        row2 = ''
        while arr2[i] > 0:
            row2 = str(arr2[i] % 2) + row2
            arr2[i] = arr2[i] // 2
        while len(row2) < n:
            row2 = '0' + row2
        arr2_bin.append(row2)
        
        answer_row = ''

        for j in range(n):
            if arr1_bin[i][j] == '1' or arr2_bin[i][j] == '1':
                answer_row += '#'
            else:
                answer_row += ' '

        answer.append(answer_row)

    return answer