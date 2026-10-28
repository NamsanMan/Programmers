def solution(record):
    answer = []
    record_class = []
    id_dict = {}
    
    for i in range(len(record)):
        row = record[i].split()
        record_class.append(row)
        id_dict[record_class[i][1]] = ''
        
    for i in range(len(record_class)): 
        if record_class[i][0] == 'Enter':
            id_dict[record_class[i][1]] = record_class[i][2]
        if record_class[i][0] == 'Change':
            id_dict[record_class[i][1]] = record_class[i][2]
        
    for i in range(len(record_class)):
        if record_class[i][0] == 'Enter':
            enter_massage = id_dict[record_class[i][1]] + '님이 들어왔습니다.'
            answer.append(enter_massage)
        elif record_class[i][0] == 'Leave':
            leave_massage = id_dict[record_class[i][1]] + '님이 나갔습니다.'
            answer.append(leave_massage)
            
    return answer