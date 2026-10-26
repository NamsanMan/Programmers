from collections import deque
def solution(msg):
    answer = []
    dictionary = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letters = deque(msg)
    w = ''
    while letters:
        w += letters.popleft()
        if letters and w + letters[0] in dictionary:
            continue
        if w in dictionary:
            answer.append(dictionary.index(w) + 1)
            if letters:
                dictionary.append(w + letters[0])
            w = ''
            
    
    return answer