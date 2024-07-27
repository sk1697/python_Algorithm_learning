'''
SWEA 5656
'''
def crash(x, y, arr):
    for dx in range(h):
        nx = x + dx
        # print("nx : ",nx)
        if nx < h and arr[nx][y] != 0:
            return nx, y

    return x, y


from collections import deque
import copy


def bfs(i, j, arr):
    q = deque()
    i, j = crash(i, j, arr)
    q.append((i, j, [(i, j)]))
    visited = [[False] * w for _ in range(h)]

    while q:
        x, y, del_pos = q.popleft()
        visited[x][y] = True
        rng = arr[x][y]

        # print(f"x={x},y={y},rng={rng}")
        # print("del_pos1 : ",del_pos)
        # 상/하 방향 확인
        for dx in range(-rng + 1, rng):
            nx = x + dx
            if 0 <= nx < h and arr[nx][y] != 0 and not visited[nx][y]:
                visited[nx][y] = True
                del_pos.append((nx, y))
                q.append((nx, y, del_pos))

        # 좌/우 방향 확인
        for dy in range(-rng + 1, rng):
            ny = y + dy
            if 0 <= ny < w and arr[x][ny] != 0 and not visited[x][ny]:
                visited[x][ny] = True
                del_pos.append((x, ny))
                q.append((x, ny, del_pos))

    # print(f"del_pos : {del_pos}")
    return del_pos


def arrange_graph(arr):
    for y in range(w):
        for x in range(h - 1, 0, -1):
            if arr[x][y] == 0:
                nx = x
                # print(f"arrange x={x} , y={y}")
                while nx > 0:
                    nx -= 1
                    if arr[nx][y] != 0:
                        arr[x][y] = arr[nx][y]
                        arr[nx][y] = 0
                        break
    # print("arranged_graph : ",arr)
    return arr


def dfs(x, y, arr, depth):
    global global_ans
    # 종료 조건
    zero_sum_flag = True if sum(sum(row) for row in arr) == 0 else False
    if depth == n or zero_sum_flag:
        # print(f"dfs x={x} , y={y}")
        # print('graph : ',arr )
        cnt = 0
        for row in arr:
            cnt += len([el for el in row if el != 0])
        # print("cnt : ",cnt)
        global_ans = min(global_ans, cnt)
        return

    # print("del_graph : ",graph)

    for ww in range(w):
        copy_arr = copy.deepcopy(arr)
        # print(f"for문 x={x} , y={ww} , depth={depth}")
        # print("arr : ", arr)
        del_lst = bfs(x, ww, arr)
        # print("del_lst : ",del_lst)
        for i, j in del_lst:
            arr[i][j] = 0
        adj_graph = arrange_graph(arr)
        # print("adj_graph : ", adj_graph)

        dfs(x, ww, adj_graph, depth + 1)
        arr = copy_arr


tc = int(input())
for case in range(1, tc + 1):
    n, w, h = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(h)]
    # 구슬과 구슬 놓은 횟수 초기화
    x, y, depth = 0, 0, 0
    global_ans = 200

    dfs(x, y, graph, depth)
    print(f"#{case} {global_ans}")