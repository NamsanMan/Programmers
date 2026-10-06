def solution(A,B):
    answer = 0
    sorted_A = sorted(A)
    sorted_B = sorted(B)
    
    for i in range(len(sorted_B)):
        answer += sorted_A[i] * sorted_B[len(sorted_B) - 1 - i]
    return answer