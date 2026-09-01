def solution(myString, pat):
    answer = ""
    for x in myString:
        if x == "A":
            answer += "B"
        elif x == "B":
            answer += "A"
            
    return int(pat in answer)