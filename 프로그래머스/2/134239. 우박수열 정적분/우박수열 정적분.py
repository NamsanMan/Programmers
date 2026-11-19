def solution(k, ranges):
    answer = []
    new_k = k
    graph = []
    while new_k > 1:
        graph.append(new_k)
        if new_k % 2 == 0:
            new_k = new_k // 2
        else:
            new_k = new_k * 3 + 1
    graph.append(new_k)
    
    n = len(graph) - 1
    for a, b in ranges:
        b = n + b
        val = 0
        if a > b:
            answer.append(-1)
        else:
            for x in range(a, b):
                val += ((graph[x] + graph[x + 1]) / 2)
            answer.append(val)
    
    return answer