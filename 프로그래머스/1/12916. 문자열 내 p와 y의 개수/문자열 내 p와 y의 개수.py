def solution(s):
    answer = True
    
    text = s.lower()
    
    p_count = 0
    y_count = 0
    
    p_count = text.count("p")
    y_count = text.count("y")
    
    if p_count == y_count:
        return True
    else:
        return False