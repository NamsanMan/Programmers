def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)

    def dfs(fatigue, count):
        nonlocal answer

        # 지금까지 간 던전 수 기록
        if count > answer:
            answer = count

        # 다음에 갈 던전을 하나씩 골라봄
        for i in range(len(dungeons)):
            need = dungeons[i][0]
            use = dungeons[i][1]

            # 아직 안 갔고, 입장 피로도가 충분하면
            if visited[i] == False and fatigue >= need:
                visited[i] = True

                # 해당 던전을 갔다고 가정하고 계속 탐색
                dfs(fatigue - use, count + 1)

                # 다른 순서도 확인해야 하므로 방문 기록 취소
                visited[i] = False

    dfs(k, 0)

    return answer