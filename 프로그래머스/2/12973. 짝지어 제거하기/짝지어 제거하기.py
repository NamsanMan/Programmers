def solution(s):
    stack = []
    
    for i in range(len(s)):
        stack.append(s[i])
        
        while len(stack) > 1 and stack[-2] == stack[-1]:
            stack.pop()
            stack.pop()
            
    if stack == []:
        return 1
    else:
        return 0