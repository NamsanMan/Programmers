import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[1] = 0
    pq = [(0, 1)]                        # (누적 시간, 마을)
    while pq:
        d, x = heapq.heappop(pq)         # 가장 시간이 짧은 마을부터
        if d > dist[x]:
            continue                     # 이미 더 짧은 경로로 처리된 항목
        for y, c in graph[x]:
            if d + c < dist[y]:          # 더 짧은 경로를 찾으면 갱신
                dist[y] = d + c
                heapq.heappush(pq, (dist[y], y))

    return sum(1 for i in range(1, N + 1) if dist[i] <= K)