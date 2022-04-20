def move():
    global dice, dice_idx

    for i in range(k):
        # 맵 이동
        next_x = now[0] + dx[dir[i]]
        next_y = now[1] + dy[dir[i]]

        if not(0 <= next_x < n and 0 <= next_y < m):
            continue

        else:
            # 동쪽 이동
            if dir[i] == 1:
                dice_idx = [0, dice_idx[4], dice_idx[2], dice_idx[1], dice_idx[6], dice_idx[5], dice_idx[3]]
        
            # 서쪽 이동
            elif dir[i] == 2:
                dice_idx = [0, dice_idx[3], dice_idx[2], dice_idx[6], dice_idx[1], dice_idx[5], dice_idx[4]]

            # 북쪽 이동
            elif dir[i] == 3:
                dice_idx = [0, dice_idx[5], dice_idx[1], dice_idx[3], dice_idx[4], dice_idx[6], dice_idx[2]]
        
            # 남쪽 이동
            else:
                dice_idx = [0, dice_idx[2], dice_idx[6], dice_idx[3], dice_idx[4], dice_idx[1], dice_idx[5]]
    
            print(dice[dice_idx[1]])

            now[0] = next_x
            now[1] = next_y

            if map_[now[0]][now[1]] == 0:
                map_[now[0]][now[1]] = dice[dice_idx[6]]
            else:
                dice[dice_idx[6]] = map_[now[0]][now[1]]
                map_[now[0]][now[1]] = 0

if __name__ == "__main__":
    n, m, x, y, k = map(int, input().split())
    map_ = []
    for _ in range(n):
        map_.append(list(map(int, input().split())))

    # 이동 방향 
    # 동: 1, 서: 2, 북: 3, 남: 4
    dir = list(map(int, input().split()))
    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]
    now = [x, y]

    # 주사위 값
    dice = [0 for _ in range(7)]

    # 주사위 인덱스
    # 1: 위, 2: 북, 3: 동, 4: 서, 5: 남, 6: 아래
    dice_idx = [0, 1, 2, 3, 4, 5, 6]

    move()