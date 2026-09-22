def solution(s, skip, index):
    answer = ''
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    
    for i in range(len(s)):
        now = alphabet.index(s[i])
        count = 0
        
        while count < index:
            now += 1
            
            if now == 26:
                now = 0
            
            if alphabet[now] not in skip:
                count += 1
        
        answer += alphabet[now]
    
    return answer