def solution(numbers):
    answer = []
    temp_arr = sorted(numbers)
    summation = 0
    for i in range(len(temp_arr)):
        for j in range(i + 1, len(temp_arr)):
            summation = temp_arr[i] + temp_arr[j]
            if summation not in answer:
                answer.append(summation)
    answer = sorted(answer)
    return answer