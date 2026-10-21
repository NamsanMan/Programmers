import heapq
def solution(scoville, K):
    answer = 0
    heap_scoville = scoville[:]
    heapq.heapify(heap_scoville)
    while heap_scoville:
        if len(heap_scoville) > 1 and heap_scoville[0] < K:
            smallest = heapq.heappop(heap_scoville)
            second_smallest = heapq.heappop(heap_scoville)
            heapq.heappush(heap_scoville, smallest + (second_smallest * 2))
            answer += 1
        elif heap_scoville[0] >= K:
            return answer
        else:
            heapq.heappop(heap_scoville)         

    return -1