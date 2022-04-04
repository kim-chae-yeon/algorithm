from collections import deque

def solution(board, snake, dir, now_dir, time):
    while True:
        time += 1
        
        next_x, next_y = snake[-1][0] + dx[now_dir], snake[-1][1] + dy[now_dir]

        # 벽이거나 뱀의 몸이면 종료
        if board[next_x][next_y] == -1 or board[next_x][next_y] == 1:
            return time

        # 사과면 머리 늘어남
        elif board[next_x][next_y] == 2:
            board[next_x][next_y] = 1
            snake.append([next_x, next_y])
        
        # 빈칸이면 꼬리 잘리고, 머리 늘어남
        else:
            tail = snake.popleft()
            board[tail[0]][tail[1]] = 0
            board[next_x][next_y] = 1
            snake.append([next_x, next_y])

        # 방향 전환 시간이면 방향 전환
        if dir:
            if time == dir[0][0]:
                if dir[0][1] == 'D':
                    now_dir = (now_dir + 1) % 4
                elif dir[0][1] == 'L':
                    now_dir = (now_dir - 1) % 4
                dir.popleft()


if __name__ == "__main__":
    size = int(input())

    # board 원소 0 초기화, 벽 -1
    board = [[0] * size for _ in range(size)]
    board.append([-1] * size)
    board.insert(0, [-1] * size)
    for x in board:
        x.append(-1)
        x.insert(0, -1)

    # 뱀 위치 1, 뱀 큐 저장
    board[1][1] = 1
    snake = deque([[1,1]])

    # 사과 위치 2로 설정
    apple_cnt = int(input())
    for _ in range(apple_cnt):
        x, y = map(int, input().split())
        board[x][y] = 2

    # 방향 변환 deque 생성 (popleft 사용위해)
    dir_cnt = int(input())
    dir = deque()
    for _ in range(dir_cnt):
        x, y = map(str, input().split())
        x = int(x)
        dir.append((x, y))

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    # 0: dx, dy 현재 index, 0: 시간
    print(solution(board, snake, dir, 0, 0))