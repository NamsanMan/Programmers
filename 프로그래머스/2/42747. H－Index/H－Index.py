def solution(citations):
    answer = 0
    new_citations = sorted(citations)
    
    for i in range(len(new_citations)):
        h = len(new_citations) - i
        if new_citations[i] >= h:
            return h
    
    return 0
        