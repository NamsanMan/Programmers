def solution(picks, minerals):
    answer = float('inf')
    # 곡갱이 하나 고르면 무조건 5번까지 사용해야됨(중간에 끝나는 경우 빼고)
    
    # idx가 5단위로 곡괭이 바꿔줘야함
    # dia, iron, ston은 각각 곡괭이를 몇번 썼는지
    # fatigue는 피로도 상태
    # cur은 현재 곡괭이. 0 dia, 1 iron, 2 stone
    def dfs(idx, dia, iron, stone, cur, fatigue):
        nonlocal answer
        # 종료 조건
        # idx가 끝났거나, 곡괭이가 더이상 없을때
        if idx == len(minerals):
            answer = min(answer, fatigue)
            return
        if idx % 5 == 0 and dia == picks[0] and iron == picks[1] and stone == picks[2]:
            answer = min(answer, fatigue)
            return
        
        # 5번 이용했는지 검사(곡괭이 바꿀지)
        if idx % 5 == 0:
            if dia < picks[0]:
                dfs(idx + 1, dia + 1, iron, stone, 0, fatigue + 1)
            if iron < picks[1]:
                if minerals[idx] == "diamond":
                    dfs(idx + 1, dia, iron + 1, stone, 1, fatigue + 5)
                else:
                    dfs(idx + 1, dia, iron + 1, stone, 1, fatigue + 1)
            if stone < picks[2]:
                if minerals[idx] == "diamond":
                    dfs(idx + 1, dia, iron, stone + 1, 2, fatigue + 25)
                elif minerals[idx] == "iron":
                    dfs(idx + 1, dia, iron, stone + 1, 2, fatigue + 5)
                else:
                    dfs(idx + 1, dia, iron, stone + 1, 2, fatigue + 1)
                
        # 곡괭이를 안바꿈
        else:
            if cur == 0:
                dfs(idx + 1, dia, iron, stone, cur, fatigue + 1)
            elif cur == 1:
                if minerals[idx] == "diamond":
                    dfs(idx + 1, dia, iron, stone, cur, fatigue + 5)
                else:
                    dfs(idx + 1, dia, iron, stone, cur, fatigue + 1)
            elif cur == 2:
                if minerals[idx] == "diamond":
                    dfs(idx + 1, dia, iron, stone, cur, fatigue + 25)
                elif minerals[idx] == "iron":
                    dfs(idx + 1, dia, iron, stone, cur, fatigue + 5)
                else:
                    dfs(idx + 1, dia, iron, stone, cur, fatigue + 1)
        
    dfs(0, 0, 0, 0, -1, 0)
    return answer