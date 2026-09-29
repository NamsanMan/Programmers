def solution(board, moves):
    answer = 0
    bucket = []
    
    new_board = board[:]
    
    for i in moves:
        for j in range(len(board)):
            if new_board[j][i - 1] != 0:
                bucket.append(new_board[j][i - 1])
                new_board[j][i - 1] = 0
                if len(bucket) > 1:
                    if bucket[-1] == bucket[-2]:
                        bucket.pop(-1)
                        bucket.pop(-1)
                        answer += 2
                break
    
    print(new_board)
    return answer