def solution(arr):
    answer = [0, 0]
    
    def compress(r, c, size):
        first_number = arr[r][c]
        for i in range(r, r + size):
            for j in range(c, c + size):
                if arr[i][j] != first_number:
                    half = size // 2
                    compress(r, c, half)
                    compress(r, c + half, half)
                    compress(r + half, c, half)
                    compress(r + half, c + half, half)
                    return
        answer[first_number] += 1
    
    compress(0, 0, len(arr))
    return answer