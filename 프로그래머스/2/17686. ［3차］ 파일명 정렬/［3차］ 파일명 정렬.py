def solution(files):
    answer = []
    numbers = set("0123456789")
    filtered_files = []
    for i in range(len(files)):
        row = []
        HEAD_row = ''
        NUMBER_row = ''
        flag = False
        for j in range(len(files[i])):
            if files[i][j] not in numbers:
                if flag:
                    break
                else:
                    HEAD_row += files[i][j].lower()
            else:
                NUMBER_row += files[i][j]
                flag = True
        row.append(HEAD_row)
        row.append(int(NUMBER_row))
        row.append(i)
        filtered_files.append(row)
                
    filtered_files.sort()
    for row in filtered_files:
        answer.append(files[row[2]])
    
    return answer