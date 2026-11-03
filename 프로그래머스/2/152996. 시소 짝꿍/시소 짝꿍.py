def solution(weights):
    answer = 0
    weight_dict = {}
    for w in weights:
        if w not in weight_dict:
            weight_dict[w] = 1
        else:
            weight_dict[w] += 1
            
    print(weight_dict)
    return answer