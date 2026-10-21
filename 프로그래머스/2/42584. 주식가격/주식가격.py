def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        while stack and stack[-1][0] > prices[i]:
            answer[stack[-1][1]] = i - stack[-1][1]
            stack.pop()
        stack.append([prices[i], i])
    
    while stack:
        index = stack.pop()[1]
        answer[index] = len(prices) - index - 1
            
    
    return answer