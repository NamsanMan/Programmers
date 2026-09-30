def solution(players, callings):
    answer = players[:]
    position = {}

    # 선수 이름별 현재 등수(인덱스) 저장
    for i in range(len(answer)):
        position[answer[i]] = i

    for name in callings:
        called_index = position[name]
        front_guy_name = answer[called_index - 1]

        # 리스트에서 두 선수 자리 교환
        answer[called_index - 1] = name
        answer[called_index] = front_guy_name

        # 딕셔너리의 등수도 갱신
        position[name] = called_index - 1
        position[front_guy_name] = called_index

    return answer