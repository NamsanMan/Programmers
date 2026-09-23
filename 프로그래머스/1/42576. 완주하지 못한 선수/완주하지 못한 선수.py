def solution(participant, completion):
    dict_comp = {}

    # 참가자 이름별 인원 수 세기
    for name in participant:
        if name in dict_comp:
            dict_comp[name] += 1
        else:
            dict_comp[name] = 1

    # 완주자는 1명씩 빼기
    for name in completion:
        dict_comp[name] -= 1

    # 값이 1인 사람이 완주하지 못한 사람
    for name in dict_comp:
        if dict_comp[name] == 1:
            return name