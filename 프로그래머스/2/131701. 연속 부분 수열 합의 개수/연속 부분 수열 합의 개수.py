def solution(elements):
    answer = set()
    extended = elements * 2
    
    prefix_sum = [0]
    
    for num in extended:
        prefix_sum.append(prefix_sum[-1] + num)
    
    print(prefix_sum)
    for length in range(1, len(elements) + 1):
        for start in range(len(elements)):
            summation = prefix_sum[start + length] - prefix_sum[start]
            answer.add(summation)
    
    return len(answer)