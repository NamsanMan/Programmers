def solution(myString):
    answer = ''
    for i in range(len(myString)):
        if myString[i] == "a" or myString[i] == "b" or myString[i] == "c" or myString[i] == "d" or myString[i] == "e" or myString[i] == "f" or myString[i] == "g" or myString[i] == "h" or myString[i] == "i" or myString[i] == "j" or myString[i] == "k":
            answer += "l"
        else:
            answer += myString[i]
    return answer