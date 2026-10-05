def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len_time = int(video_len[0:2]) * 60 + int(video_len[3:])
    pos_time = int(pos[0:2]) * 60 + int(pos[3:])
    op_start_time = int(op_start[0:2]) * 60 + int(op_start[3:])
    op_end_time = int(op_end[0:2]) * 60 + int(op_end[3:])
    
    for x in commands:
        if pos_time >= op_start_time and pos_time <= op_end_time:
            pos_time = op_end_time
        if x == "next":
            if pos_time + 10 >= op_start_time and pos_time + 10 <= op_end_time:
                pos_time = op_end_time
            elif pos_time + 10 >= video_len_time:
                pos_time = video_len_time
            else:
                pos_time = pos_time + 10
        elif x == "prev":
            if pos_time - 10 >= op_start_time and pos_time - 10 <= op_end_time:
                pos_time = op_end_time
            elif pos_time - 10 <= 0:
                pos_time = 0
            else:
                pos_time = pos_time - 10
                
    pos_time_mm = pos_time // 60
    pos_time_ss = pos_time % 60
    
    if pos_time_mm < 10:
        answer += '0' + str(pos_time_mm)
    else:
        answer += str(pos_time_mm)
    
    answer += ":"
    
    if pos_time_ss < 10:
        answer += '0' + str(pos_time_ss)
    else:
        answer += str(pos_time_ss)
    
    return answer