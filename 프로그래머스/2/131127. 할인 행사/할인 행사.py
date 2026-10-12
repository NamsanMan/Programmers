def solution(want, number, discount):
    answer = 0
    want_dict = {}
    discount_dict = {}
    
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    
    for i in range(10, len(discount) + 1):
        for x in range(len(want)):
            discount_dict[want[x]] = 0
        for j in range(i - 10, i):
            if discount[j] in discount_dict:
                discount_dict[discount[j]] += 1
        if want_dict == discount_dict:
            answer += 1
    return answer