def solution(progresses, speeds):
    answer = []
    ID_progresses = {}
    for i in range(len(progresses)):
        ID_progresses[i] = progresses[i]
    
    completed_ID = []
    days = 0
    while len(completed_ID) < len(progresses):
        days += 1
        count = 0
        for i in range(len(ID_progresses)):
            ID_progresses[i] += speeds[i]
        for i in range(len(completed_ID), len(ID_progresses)):
            if ID_progresses[i] < 100:
                break
            else:
                count += 1
                completed_ID.append(i)
        if count > 0:
            answer.append(count)
    print(ID_progresses)
    return answer