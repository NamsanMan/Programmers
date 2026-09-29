def solution(schedules, timelogs, startday):
    answer = 0
    valiate_timlogs = []
    
    def to_minutes(time):
        hour = time // 100
        minute = time % 100
        return hour * 60 + minute
    
    for i in range(len(timelogs)):
        row = []
        day = startday
        for j in range(len(timelogs[i])):
            if day <= 5 and day >= 1:
                row.append(timelogs[i][j])
            elif day == 7:
                day = 0
            day = day + 1
        valiate_timlogs.append(row)
    
    for i in range(len(valiate_timlogs)):
        no_flag = False
        for j in range(len(valiate_timlogs[i])):
            if to_minutes(valiate_timlogs[i][j]) > to_minutes(schedules[i]) + 10:
                no_flag = True
        if no_flag == False:
            answer += 1
    
    return answer