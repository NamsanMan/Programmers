def name_map(input_name, matching_name, y):
    for i in range(len(matching_name)):
        if input_name == matching_name[i]:
            return y[i]

def solution(name, yearning, photo):
    answer = []
    memory_only = []
    int_mem = []
    for i in range(len(photo)):
        row = []
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                row.append(photo[i][j])
        memory_only.append(row)
    
    for i in range(len(memory_only)):
        row = []
        for j in range(len(memory_only[i])):
            row.append(name_map(memory_only[i][j], name, yearning))
        int_mem.append(row)
    for i in range(len(int_mem)):
        summation = 0
        for j in range(len(int_mem[i])):
            summation += int_mem[i][j]
        answer.append(summation)
    print(answer)
    return answer