'''
SWEA 1953

BFS로 연결 가능한 터널을 체크하면서 마지막에 터널 개수 카운트,
testcase 49 fail이었는데, L=1인 경우는 1개를 출력해야되는 부분 놓쳤었음.

'''
from collections import deque
tc = int(input())
for case in range(1 , tc+1):
    N,M,R,C,L = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    type = {1:[[-1,0],[0,1],[1,0],[0,-1]],
            2:[[-1,0],[1,0]],
            3:[[0,1],[0,-1]],
            4:[[-1,0],[0,1]],
            5:[[0,1],[1,0]],
            6:[[1,0],[0,-1]],
            7:[[-1,0],[0,-1]]}


    def bfs():
        q = deque()
        q.append([R,C])
        visited[R][C] = 1

        while q:
            cx, cy = q.popleft()

            for dx,dy in type[arr[cx][cy]]:
                nx = cx +dx
                ny = cy + dy

                if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                    if arr[nx][ny] == 0: continue
                    check = False
                    for tx,ty in type[arr[nx][ny]]:
                        if (nx + tx) ==cx and (ny + ty) == cy:
                            check = True

                    if not check: continue

                    visited[nx][ny] = visited[cx][cy] +1
                    if visited[nx][ny] < L:
                        q.append([nx,ny])

    visited = [[0]*M for _ in range(N)]
    bfs()

    # print("visited")
    # for i in range(N):
    #     print(*visited[i])

    if L == 1:
        print(f"#{case} 1")
    else:
        cnt = 0
        for i in range(N):
            for j in range(M):
                if visited[i][j] !=0:
                    cnt +=1
        print(f"#{case} {cnt}")