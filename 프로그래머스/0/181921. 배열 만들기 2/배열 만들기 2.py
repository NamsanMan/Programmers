def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if all(x == "0" or x == "5" for x in str(i)):
            answer.append(i)
            
    if answer == []:
        return [-1]
            
    return answer