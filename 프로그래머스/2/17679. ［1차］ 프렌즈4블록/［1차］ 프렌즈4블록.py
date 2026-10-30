def solution(m, n, board):
    answer = 0
    new_board = [list(row) for row in board]
    continue_game = True

    while continue_game:
        # 매 라운드마다 표시판을 초기화
        check_board = []
        for i in range(m):
            row = ["X"] * n
            check_board.append(row)

        # 지울 블록 표시
        for y in range(m - 1):
            for x in range(n - 1):
                if (new_board[y][x] != ""
                    and new_board[y][x] == new_board[y][x + 1]
                    == new_board[y + 1][x]
                    == new_board[y + 1][x + 1]):

                    check_board[y][x] = "O"
                    check_board[y][x + 1] = "O"
                    check_board[y + 1][x] = "O"
                    check_board[y + 1][x + 1] = "O"

        # 표시된 블록을 한꺼번에 지우기
        removed = 0
        for y in range(m):
            for x in range(n):
                if check_board[y][x] == "O":
                    new_board[y][x] = ""
                    removed += 1

        # 지워진 블록이 없으면 종료
        if removed == 0:
            continue_game = False
            break

        answer += removed

        # 각 열에서 남은 블록을 모아 아래부터 채우기
        for x in range(n):
            blocks = []
            for y in range(m):
                if new_board[y][x] != "":
                    blocks.append(new_board[y][x])

            for y in range(m - 1, -1, -1):
                if blocks:
                    new_board[y][x] = blocks.pop()
                else:
                    new_board[y][x] = ""

    return answer