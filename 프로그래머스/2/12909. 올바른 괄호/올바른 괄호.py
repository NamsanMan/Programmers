def solution(s):
    answer = True
    stack = []

    for i in range(len(s)):
        if s[i] == "(":
            stack.append("(")
            
        else:
            if stack == []:
                return False
            
            stack.pop()
    
    if stack == []:
        return True

    else:
        return False