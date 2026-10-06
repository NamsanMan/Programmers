def solution(s):
    answer = ''
    temp = s.split(" ")
    for i in range(len(temp)):
        temp[i] = int(temp[i])
        
    answer = str(min(temp)) + " " + str(max(temp))
    return answer