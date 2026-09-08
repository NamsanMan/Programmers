def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        row = ""
        for j in range(len(picture[i])):
            for _ in range(k):
                row += picture[i][j]
        
        for _ in range(k):
            answer.append(row)
    return answer