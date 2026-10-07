def solution(s):
    answer = ''
    is_first_letter = True
    for i in range(len(s)):
        if s[i] == " ":
            answer += " "
            is_first_letter = True
        else:
            if is_first_letter == True:
                answer += s[i].upper()
                is_first_letter = False
            else:
                answer += s[i].lower()
                
                
        
    return answer