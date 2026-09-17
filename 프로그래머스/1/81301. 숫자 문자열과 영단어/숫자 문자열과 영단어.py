def solution(s):
    answer = ''
    stack = ''
    for i in range(len(s)):
        stack += s[i]
                
        if (stack == 'zero'):
            answer += '0'
            stack = ''
            
        if (stack == 'one'):
            answer += '1'
            stack = ''
        if (stack == 'two'):
            answer += '2'
            stack = ''
        if (stack == 'three'):
            answer += '3'
            stack = ''
        if (stack == 'four'):
            answer += '4'
            stack = ''
        if (stack == 'five'):
            answer += '5'
            stack = ''
        if (stack == 'six'):
            answer += '6'
            stack = ''
        if (stack == 'seven'):
            answer += '7'
            stack = ''
        if (stack == 'eight'):
            answer += '8'
            stack = ''
        if (stack == 'nine'):
            answer += '9'
            stack = ''
        if stack == '0' or stack == '1' or stack == '2' or stack == '3' or stack == '4' or stack == '5' or stack == '6' or stack == '7' or stack == '8' or stack == '9':
            answer += stack
            stack = ''
    return int(answer)