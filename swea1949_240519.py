'''
SWEA 1949


'''
from collections import deque
import copy

tc = int(input())
for case in range(1,tc+1):

    n,k = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(n)]

    #그래프의 최고 높이
    max_height = max([max(row) for row in graph])
    # print(max([max(row) for row in graph]))

    # 최고 높이 좌표
    max_height_pos = []
    for i in range(n):
        for j in range(n):
            if graph[i][j]==max_height:
                max_height_pos.append((i,j))

    # print("max_height_pos : ",max_height_pos)

    d = [(-1,0),(0,1),(1,0),(0,-1)]
    def bfs(arr,x,y):
        q = deque()
        q.append((x,y,1))

        while q:
            x, y,dist = q.popleft()

            # print(f"nx : {x}, ny : {y}, dist : {dist}")

            for dx, dy in d:
                nx = x + dx
                ny = y + dy

                if 0<=nx<n and 0<=ny<n and arr[nx][ny]< arr[x][y]:
                    # visited[nx][ny] = True
                    q.append((nx,ny,dist+1))


        return dist




    max_dist = 0
    for i in range(n):
        for j in range(n):
            for kk in range(1,k+1):
                maps = copy.deepcopy(graph)
                maps[i][j] -= kk
                # print(f"i = {i} , j = {j}")
                # print("maps : ",maps)
                for pos in max_height_pos:
                    if pos[0]==i and pos[1]==j: continue


                    # visited = [[False] * n for _ in range(n)]
                    dist = bfs(maps,pos[0],pos[1])
                    # print("dist : ",dist)
                    max_dist = max(max_dist,dist)

    print(f"#{case} {max_dist}")
