import sys
from copy import deepcopy
sys.setrecursionlimit(10 ** 6)

# 전치함수 (행열 바꾸기)
def transpose(a):
    a = list(map(list, zip(*a)))
    return a

# 0 제거 (미는 방향쪽으로 채우기)
# 위, 왼쪽: 1, 아래, 오른쪽: 2
def del_empty(dir, a):
    for x in range(n):
        for y in range(n):
            cnt = 1
            while a[x][y] == 0 and cnt <= n - y:
                a[x].pop(y)
                if dir == 1:
                    a[x].append(0)
                else:
                    a[x].insert(0, 0)
                cnt += 1
            
def DFS(dir, cnt, a):
    global max_block

    if cnt == 6:
        now_max = max(map(max, a))
        if max_block < now_max:
            max_block = now_max
        return

    else:
        # 위, 아래 방향이면 전치
        if dir == 1 or dir == 3:
            a = transpose(a)
            
        
        # 위, 왼쪽인 경우 왼쪽부터 탐색
        if dir == 1 or dir == 2:
            del_empty(1, a)
            
            for x in range(n):
                flag = False
                for y in range(n-1):
                    if flag == True:
                        flag = False
                        continue
                        
                    if a[x][y] == a[x][y+1]:
                        a[x][y] *= 2
                        a[x][y+1] = 0
                        flag = True
                 
            del_empty(1, a)

        # 아래, 오른쪽인 경우 오른쪽부터 탐색
        else:
            del_empty(2, a)
            for x in range(n):
                flag = False
                for y in range(n-1, 0, -1):
                    if flag == True:
                        flag = False
                        continue

                    if a[x][y] == a[x][y-1]:
                        a[x][y] *= 2 
                        a[x][y-1] = 0
                        flag = True
            del_empty(2, a)
            

        # 위, 아래 방향이면 다시 전치
        if dir == 1 or dir == 3:
            a = transpose(a)
            
        # 재귀호출
        for d in range(1, 5):
            DFS(d, cnt + 1, deepcopy(a))


if __name__ == "__main__":
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    max_block = 0
    # 위: 1, 왼쪽: 2, 아래: 3, 오른쪽: 4
    for i in range(1, 5):
        DFS(i, 1, deepcopy(a))

    print(max_block)    