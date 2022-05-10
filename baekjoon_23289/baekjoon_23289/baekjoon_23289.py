import sys
from collections import deque
def right_wind(x, y):
    global map_

    # 시작점
    map_[x][y+1] += 5
    queue = deque([(x, y+1)])
    value = 4
    # 방문 노드
    check = []
    while queue and value > 0:
        size = len(queue)
        for _ in range(size):
            now = queue.popleft()
            # 1: 오른쪽, 2: 왼쪽, 3: 위, 4: 아래
            # x-1, y 기준 아래, 오른쪽에 벽 없으면 
            if not (now[0]-1, now[1]+1) in check and 0<=now[0]-1<r and 0<=now[1]+1<c:
                if (now[0]-1, now[1]) in wall:
                    if not(1 in wall[(now[0]-1, now[1])] or 4 in wall[(now[0]-1, now[1])]):
                        map_[now[0]-1][now[1]+1] += value
                        queue.append((now[0]-1, now[1]+1))
                        check.append((now[0]-1, now[1]+1))
                else:
                    map_[now[0]-1][now[1]+1] += value
                    queue.append((now[0]-1, now[1]+1))
                    check.append((now[0]-1, now[1]+1))
            # x, y 기준 오른쪽에 벽 없으면 갱신
            if not (now[0], now[1]+1) in check and 0<=now[0]<r and 0<=now[1]+1<c:
                if (now[0], now[1]) in wall:
                    if not 1 in wall[(now[0], now[1])]:
                        map_[now[0]][now[1]+1] += value
                        queue.append((now[0], now[1]+1))
                        check.append((now[0], now[1]+1))
                else:
                    map_[now[0]][now[1]+1] += value
                    queue.append((now[0], now[1]+1))
                    check.append((now[0], now[1]+1))
            # x+1, y 기준 위, 오른쪽에 벽 없으면 갱신
            if not (now[0]+1, now[1]+1) in check and 0<=now[0]+1<r and 0<=now[1]+1<c:
                if (now[0]+1, now[1]) in wall:
                    if not(1 in wall[(now[0]+1, now[1])] or 3 in wall[(now[0]+1, now[1])]):
                        map_[now[0]+1][now[1]+1] += value
                        queue.append((now[0]+1, now[1]+1))
                        check.append((now[0]+1, now[1]+1))
                else:
                    map_[now[0]+1][now[1]+1] += value
                    queue.append((now[0]+1, now[1]+1))
                    check.append((now[0]+1, now[1]+1))

        value -= 1
        check = []

def left_wind(x, y):
    global map_

    # 시작점
    map_[x][y-1] += 5
    queue = deque([(x, y-1)])
    value = 4
    # 방문 노드
    check = []
    while queue and value > 0:
        size = len(queue)
        for _ in range(size):
            now = queue.popleft()
            # 1: 오른쪽, 2: 왼쪽, 3: 위, 4: 아래
            # x-1, y 기준 아래, 왼쪽에 벽 없으면 갱신
            if not (now[0]-1, now[1]-1) in check and 0<=now[0]-1<r and 0<=now[1]-1<c:
                if (now[0]-1, now[1]) in wall:
                    if not(2 in wall[(now[0]-1, now[1])] or 4 in wall[(now[0]-1, now[1])]):
                        map_[now[0]-1][now[1]-1] += value
                        queue.append((now[0]-1, now[1]-1))
                        check.append((now[0]-1, now[1]-1))
                else:
                    map_[now[0]-1][now[1]-1] += value
                    queue.append((now[0]-1, now[1]-1))
                    check.append((now[0]-1, now[1]-1))
            # x, y 기준 왼쪽에 벽 없으면 갱신
            if not (now[0], now[1]-1) in check and 0<=now[0]<r and 0<=now[1]-1<c:
                if (now[0], now[1]) in wall:
                    if not 2 in wall[(now[0], now[1])]:
                        map_[now[0]][now[1]-1] += value
                        queue.append((now[0], now[1]-1))
                        check.append((now[0], now[1]-1))
                else:
                    map_[now[0]][now[1]-1] += value
                    queue.append((now[0], now[1]-1))
                    check.append((now[0], now[1]-1))
            # x+1, y 기준 위, 왼쪽에 벽 없으면 갱신
            if not (now[0]+1, now[1]-1) in check and 0<=now[0]+1<r and 0<=now[1]-1<c:
                if (now[0]+1, now[1]) in wall:
                    if not(2 in wall[(now[0]+1, now[1])] or 3 in wall[(now[0]+1, now[1])]):
                        map_[now[0]+1][now[1]-1] += value
                        queue.append((now[0]+1, now[1]-1))
                        check.append((now[0]+1, now[1]-1))
                else:
                    map_[now[0]+1][now[1]-1] += value
                    queue.append((now[0]+1, now[1]-1))
                    check.append((now[0]+1, now[1]-1))

        value -= 1
        check = []

def up_wind(x, y):
    global map_

    # 시작점
    map_[x-1][y] += 5
    queue = deque([(x-1, y)])
    value = 4
    # 방문 노드
    check = []
    while queue and value > 0:
        size = len(queue)
        for _ in range(size):
            now = queue.popleft()
            # 1: 오른쪽, 2: 왼쪽, 3: 위, 4: 아래
            # x, y-1 기준 위, 오른쪽에 벽 없으면 갱신
            if not (now[0]-1, now[1]-1) in check and 0<=now[0]-1<r and 0<=now[1]-1<c:
                if (now[0], now[1]-1) in wall:
                    if not(1 in wall[(now[0], now[1]-1)] or 3 in wall[(now[0], now[1]-1)]):
                        map_[now[0]-1][now[1]-1] += value
                        queue.append((now[0]-1, now[1]-1))
                        check.append((now[0]-1, now[1]-1))
                else:
                    map_[now[0]-1][now[1]-1] += value
                    queue.append((now[0]-1, now[1]-1))
                    check.append((now[0]-1, now[1]-1))
            # x, y 기준 위에 벽 없으면 갱신
            if not (now[0]-1, now[1]) in check and 0<=now[0]-1<r and 0<=now[1]<c:
                if (now[0], now[1]) in wall:
                    if not 3 in wall[(now[0], now[1])]:
                        map_[now[0]-1][now[1]] += value
                        queue.append((now[0]-1, now[1]))
                        check.append((now[0]-1, now[1]))
                else:
                    map_[now[0]-1][now[1]] += value
                    queue.append((now[0]-1, now[1]))
                    check.append((now[0]-1, now[1]))
            # x, y+1 기준 위, 왼쪽에 벽 없으면 갱신
            if not (now[0]-1, now[1]+1) in check and 0<=now[0]-1<r and 0<=now[1]+1<c:
                if (now[0], now[1]+1) in wall:
                    if not(2 in wall[(now[0], now[1]+1)] or 3 in wall[(now[0], now[1]+1)]):
                        map_[now[0]-1][now[1]+1] += value
                        queue.append((now[0]-1, now[1]+1))
                        check.append((now[0]-1, now[1]+1))
                else:
                    map_[now[0]-1][now[1]+1] += value
                    queue.append((now[0]-1, now[1]+1))
                    check.append((now[0]-1, now[1]+1))

        value -= 1
        check = []

def down_wind(x, y):
    global map_

    # 시작점
    map_[x+1][y] += 5
    queue = deque([(x+1, y)])
    value = 4
    # 방문 노드
    check = []
    while queue and value > 0:
        size = len(queue)
        for _ in range(size):
            now = queue.popleft()
            # 1: 오른쪽, 2: 왼쪽, 3: 위, 4: 아래
            # x, y-1 기준 아래, 오른쪽에 벽 없으면 갱신
            if not (now[0]+1, now[1]-1) in check and 0<=now[0]+1<r and 0<=now[1]-1<c:
                if (now[0], now[1]-1) in wall:
                    if not(1 in wall[(now[0], now[1]-1)] or 4 in wall[(now[0], now[1]-1)]):
                        map_[now[0]+1][now[1]-1] += value
                        queue.append((now[0]+1, now[1]-1))
                        check.append((now[0]+1, now[1]-1))
                else:
                    map_[now[0]+1][now[1]-1] += value
                    queue.append((now[0]+1, now[1]-1))
                    check.append((now[0]+1, now[1]-1))
            # x, y 기준 아래에 벽 없으면 갱신
            if not (now[0]+1, now[1]) in check and 0<=now[0]+1<r and 0<=now[1]<c:
                if (now[0], now[1]) in wall:
                    if not 4 in wall[(now[0], now[1])]:
                        map_[now[0]+1][now[1]] += value
                        queue.append((now[0]+1, now[1]))
                        check.append((now[0]+1, now[1]))
                else:
                    map_[now[0]+1][now[1]] += value
                    queue.append((now[0]+1, now[1]))
                    check.append((now[0]+1, now[1]))
            # x, y+1 기준 아래, 왼쪽에 벽 없으면 갱신
            if not (now[0]+1, now[1]+1) in check and 0<=now[0]+1<r and 0<=now[1]+1<c:
                if (now[0], now[1]+1) in wall:
                    if not(2 in wall[(now[0], now[1]+1)] or 4 in wall[(now[0], now[1]+1)]):
                        map_[now[0]+1][now[1]+1] += value
                        queue.append((now[0]+1, now[1]+1))
                        check.append((now[0]+1, now[1]+1))
                else:
                    map_[now[0]+1][now[1]+1] += value
                    queue.append((now[0]+1, now[1]+1))
                    check.append((now[0]+1, now[1]+1))

        value -= 1
        check = []

def wind_func():
    for w in wind:
        if w[2] == 1:
            right_wind(w[0], w[1])
        if w[2] == 2:
            left_wind(w[0], w[1])
        if w[2] == 3:
            up_wind(w[0], w[1])
        if w[2] == 4:
            down_wind(w[0], w[1])

def balance():
    global map_
    map_gap = [[0 for _ in range(c)] for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if 0<=x<r and 0<=y+1<c and (((x, y) in wall and not 1 in wall[(x, y)]) or not (x, y) in wall):
                gap = abs(map_[x][y] - map_[x][y+1]) // 4
                if map_[x][y] > map_[x][y+1]:
                    map_gap[x][y] -= gap
                    map_gap[x][y+1] += gap
                elif map_[x][y] < map_[x][y+1]:
                    map_gap[x][y] += gap
                    map_gap[x][y+1] -= gap

            if 0<=x+1<r and 0<=y<c and (((x, y) in wall and not 4 in wall[(x, y)]) or not (x, y) in wall):
                gap = abs(map_[x][y] - map_[x+1][y]) // 4
                if map_[x][y] > map_[x+1][y]:
                    map_gap[x][y] -= gap
                    map_gap[x+1][y] += gap
                elif map_[x][y] < map_[x+1][y]:
                    map_gap[x][y] += gap
                    map_gap[x+1][y] -= gap

    for x in range(r):
        for y in range(c):
            map_[x][y] += map_gap[x][y]
            
def out_minus():
    global map_
    for x in range(r):
        for y in range(c):
            if (x == 0 or x == r-1 or y == 0 or y == c-1) and map_[x][y] > 0:
                map_[x][y] -= 1

if __name__ == "__main__":
    input = sys.stdin.readline
    # r X c 크기 map_, 조사해야되는 칸이 k도 이상
    r, c, k = map(int, input().split())
    map_ = [list(map(int, input().split())) for _ in range(r)]
    # 1: 오른쪽, 2: 왼쪽, 3: 위, 4: 아래 방향 선풍기 바람
    # wind: (x, y, t)=> (x, y)에서 t 방향으로 부는 선풍기
    # check: 조사해야될 좌표
    wind = []
    check = []
    for x in range(r):
        for y in range(c):
            if 1 <= map_[x][y] <= 4:
                wind.append((x, y, map_[x][y]))
                map_[x][y] = 0
            if map_[x][y] == 5:
                check.append((x, y))
                map_[x][y] = 0

    # 벽 개수 w, 벽 정보 (x, y, t) (t=0이면 x,y 위에 벽, t=1이면 x,y 오른쪽에 벽)
    w = int(input())
    wall = dict()
    for _ in range(w):
        x, y, t = map(int, input().split())
        # 1: 오른쪽, 2: 왼쪽, 3: 위, 4: 아래
        # idx 0~
        # t=0 이면 (x, y) 3방향, (x-1, y) 4방향 벽
        if t == 0:
            if not (x-1, y-1) in wall:
                wall[(x-1, y-1)] = [3]
            elif (x-1, y-1) in wall:
                wall[(x-1, y-1)].append(3)

            if not (x-2, y-1) in wall:
                wall[(x-2, y-1)] = [4]
            elif (x-2, y-1) in wall:
                wall[(x-2, y-1)].append(4)

        # t=1 이면 (x, y) 1방향, (x, y+1) 2방향 벽
        else:
            if not (x-1, y-1) in wall:
                wall[(x-1, y-1)] = [1]
            elif (x-1, y-1) in wall:
                wall[(x-1, y-1)].append(1)

            if not (x-1, y) in wall:
                wall[(x-1, y)] = [2]
            elif (x-1, y) in wall:
                wall[(x-1, y)].append(2)

    choco = 0
    while True:
        wind_func()
        balance()
        out_minus()
        choco += 1
        if choco > 100:
            print("101")
            break
        for ch in check:
            if map_[ch[0]][ch[1]] < k:
                break
        else:
            print(choco)
            break