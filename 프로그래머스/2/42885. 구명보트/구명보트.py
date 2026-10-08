def solution(people, limit):
    answer = 0
    sorted_ppl = sorted(people)    
    left_idx = 0
    right_idx = len(sorted_ppl) - 1
    
    while left_idx <= right_idx:
        if left_idx == right_idx:
            answer += 1
            break
        if sorted_ppl[left_idx] + sorted_ppl[right_idx] <= limit:
            left_idx += 1
        right_idx -= 1
        answer += 1
    
    return answer