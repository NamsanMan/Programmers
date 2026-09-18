def solution(answers):
    answer = []
    guess = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    num_rights = []
    
    for i in range(len(guess)):
        correct = 0
        
        if len(answers) <= len(guess[i]):
            
            for j in range(len(answers)):
                if answers[j] == guess[i][j]:
                    correct +=1
            num_rights.append(correct)
        elif len(answers) > len(guess[i]):
            while len(answers) > len(guess[i]):
                for x in range(len(guess[i])):
                    guess[i].append(guess[i][x])
            
            for j in range(len(answers)):
                if answers[j] == guess[i][j]:
                    correct +=1
            num_rights.append(correct)
            
    for i in range(len(num_rights)):
        if num_rights[i] == max(num_rights):
            answer.append(i + 1)
            
    
    print(num_rights)
    return answer