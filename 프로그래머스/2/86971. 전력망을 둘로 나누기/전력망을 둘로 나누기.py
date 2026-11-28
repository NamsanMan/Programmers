from collections import deque
def solution(n, wires):
    answer = n                                   # 수정: 최솟값이므로 큰 값에서 시작
    for i in range(len(wires)):
        connected = [False] * (n + 1)            # 수정: 1~n번 송전탑
        leftovers = []
        for j in range(len(wires)):
            if i != j:
                leftovers.append((wires[j][0], wires[j][1]))
                leftovers.append((wires[j][1], wires[j][0]))

        # 여기부터 추가: 끊은 전선의 한쪽 끝에서 출발해 닿는 송전탑 세기
        start = wires[i][0]
        connected[start] = True
        q = deque([start])
        cnt = 1
        while q:
            x = q.popleft()
            for a, b in leftovers:               # 남은 전선 중 x에서 출발하는 것
                if a == x and not connected[b]:
                    connected[b] = True
                    q.append(b)
                    cnt += 1
        answer = min(answer, abs(n - 2 * cnt))   # 한쪽 cnt, 반대쪽 n - cnt
    return answer