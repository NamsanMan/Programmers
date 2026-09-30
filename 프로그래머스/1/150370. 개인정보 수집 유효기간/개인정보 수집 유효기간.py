def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    
    # 년도에서 2000을 빼고 이용하기
    today_days = int(today[0:4]) * 12 * 28 + int(today[5:7]) * 28 + int(today[8:])
    
    for i in range(len(terms)):
        terms_dict[terms[i][0]] = int(terms[i][1:]) * 28
    
    for i in range(len(privacies)):
        privacies_days = int(privacies[i][0:4]) * 12 * 28 + int(privacies[i][5:7]) * 28 + int(privacies[i][8:10])
        due_date = privacies_days + terms_dict[privacies[i][-1]]
        if today_days >= due_date:
            answer.append(i + 1)
            
    return answer