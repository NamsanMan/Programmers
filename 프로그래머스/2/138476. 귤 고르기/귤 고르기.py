def solution(k, tangerine):
    answer = 0
    dict_tangerine = {}
    
    for i in range(len(tangerine)):
        if tangerine[i] not in dict_tangerine:
            dict_tangerine[tangerine[i]] = 0
        dict_tangerine[tangerine[i]] += 1
    
    sorted_tangerine = sorted(dict_tangerine.items(), key = lambda item : item[1], reverse = True)
    
    total_tangerine = 0
    index = 0
    while total_tangerine < k:
        if total_tangerine < k:
            total_tangerine += sorted_tangerine[index][1]
            index += 1
            answer += 1
        else:
            break
    return answer