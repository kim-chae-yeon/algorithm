import sys
from collections import deque

# 입력 값
n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(str, input())))

# 각 구슬, 구멍 위치
for i in range(n):
    for j in range(m):
        if a[i][j] == 'R':
            r = (i, j)
        if a[i][j] == 'B':
            b = (i, j)
        if a[i][j] == 'O':
            o = (i, j)

Q = deque()
Q.append((r[0], r[1], b[0], b[1]))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [(r[0], r[1], b[0], b[1])]

cnt = 1
while True:
    # 10번 시도 실패거나 Q에 노드가 없으면, -1 반환
    if cnt == 11 or not Q:
        print(-1)
        sys.exit(0)

    else:
        # Q에 있는 노드 개수만큼 BFS (같은 cnt 끼리)
        size = len(Q)

        for _ in range(size):
            now = Q.popleft()

            # 위, 오른쪽, 아래, 왼쪽 탐색
            for i in range(4):
                r_x, r_y = now[0], now[1]
                b_x, b_y = now[2], now[3]

                # 빨간 공, 파란 공 동시에 한 방향으로 갈 수 있는 만큼 나아가기
                r_cnt = 0
                while a[r_x + dx[i]][r_y + dy[i]] != "#" and (r_x, r_y) != o:
                    r_x += dx[i]
                    r_y += dy[i]
                    r_cnt += 1
                
                b_cnt = 0
                while a[b_x + dx[i]][b_y + dy[i]] != "#" and (b_x, b_y) != o:
                    b_x += dx[i]
                    b_y += dy[i]
                    b_cnt += 1

                # 파란 구슬이 구멍일 경우 -1 종료
                if (b_x, b_y) == o:
                    continue 

                # 파란 구슬이 구멍아닌데 빨간 구슬이 구멍이면 cnt 종료
                if (r_x, r_y) == o:
                    print(cnt)
                    sys.exit(0)
                
                # 같은 위치일 경우
                if r_x == b_x and r_y == b_y:
                    # 움직인 횟수가 큰 구슬을 한 칸 뒤로
                    if r_cnt > b_cnt:
                        r_x -= dx[i]
                        r_y -= dy[i]
                    else:
                        b_x -= dx[i]
                        b_y -= dy[i]
                
                if not (r_x, r_y, b_x, b_y) in visited:
                    Q.append((r_x, r_y, b_x, b_y))
                    visited.append((r_x, r_y, b_x, b_y))

    cnt += 1