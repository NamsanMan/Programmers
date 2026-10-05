def solution(id_list, report, k):
    answer = []
    report_dict = {}
    reporter_ID = []
    reported = []
    suspended_ID = []
    for _ in range(len(id_list)):
        reported.append(0)
        answer.append(0)
        
    for i in range(len(report)):
        reporter_and_reported = report[i].split(" ")
        if reporter_and_reported[0] not in reporter_ID:
            reporter_ID.append(reporter_and_reported[0])
            report_dict[reporter_and_reported[0]] = []
            report_dict[reporter_and_reported[0]].append(reporter_and_reported[1])
        else:
            if reporter_and_reported[1] not in report_dict[reporter_and_reported[0]]:
                report_dict[reporter_and_reported[0]].append(reporter_and_reported[1])
    
    for i in range(len(id_list)):
        if id_list[i] in report_dict:
            for j in range(len(report_dict[id_list[i]])):
                reported[id_list.index(report_dict[id_list[i]][j])] += 1
    for i in range(len(reported)):
        if reported[i] >= k:
            suspended_ID.append(i)
            
    if suspended_ID != []:
        for i in range(len(suspended_ID)):
            for name in report_dict:
                if id_list[suspended_ID[i]] in report_dict[name]:
                    answer[id_list.index(name)] += 1
    
    return answer