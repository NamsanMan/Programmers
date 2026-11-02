# 다리에 처음 올라간 뒤, 다리를 내려 올 때 까지 다리 길이만큼의 시간 걸림
# 초당 1개의 버스만 다리에 올라갈 수 있고, 초당 1개의 버스만 다리에서 빠져나올 수 있음
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_queue = deque([0] * bridge_length)
    truck_queue = deque(truck_weights)
    bridge_sum = 0

    while True:
        if bridge_sum == 0 and not truck_queue:
            return answer

        # 다리에서 빠져나오는 트럭 처리
        bridge_sum -= bridge_queue.popleft()

        # 대기 중인 트럭이 있고, 무게 제한을 넘지 않으면 진입
        if truck_queue and bridge_sum + truck_queue[0] <= weight:
            truck = truck_queue.popleft()
            bridge_queue.append(truck)
            bridge_sum += truck
        else:
            bridge_queue.append(0)

        answer += 1