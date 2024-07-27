'''
SWEA 2115

idea
1. 두 명의 일꾼이 가로로 M 연속하여 선택할 수 있는 모든 경우의 수를 찾아야됨
2. 두 명의 일꾼이 선택된 벌통에서 C의 값 내 가능한 최대 조합을 찾음
3. 조합에서 얻을 수 있는 최대값을 계산
'''




# def possible(x,y,arr):
#     # print(f"possible arr : {arr}")
#     if y+m >n: return False
#
#     if 0<=x<n and arr[x][y]==-1:
#         for dy in range(y,y+m) :
#             if arr[x][dy] !=-1:
#                 return False
#
#         return True
#
#     return False
#
# def set_visited(x,y,visited,cnt):
#     for dy in range(y,y+m):
#         visited[x][dy] = cnt
#
#     return visited
# def reset_visited(x,y,visited):
#     for dy in range(y,y+m):
#         visited[x][dy] = -1
#
#     return visited
#
# def calc(order,arr,r,depth,path):
#     global ans,test
#
#     if len(path)>0 and sum(path)<=c:
#         # print("calc path : ", path)
#         # print("path sum : ", sum(list(map(lambda x: x ** 2, path))))
#         # print("test[order] : ",test[order])
#         if sum(list(map(lambda x: x ** 2, path))) > sum(list(map(lambda x: x ** 2, test[order]))):
#             # print("여기 진입?",path)
#             test[order] = path.copy()
#
#     if len(arr)== depth:
#         # print("len(arr) : ",len(arr))
#         # print("depth",depth)
#         return
#
#     for i in range(r,len(arr)):
#         # print(f"i={i}, arr[i]={arr[i]} depth={depth}")
#         path.append(arr[i])
#         calc(order,arr,i+1,depth+1,path)
#         path.pop()
#
#
#
# from collections import deque
# def dfs(x,y,cnt,visited):
#     global ans,test
#
#     #종료조건
#     if cnt ==2:
#         # print(f"x={x}, y={y},visited={visited}")
#         path = {}
#         path[0] = []
#         path[1] = []
#         for i in range(n):
#             for j in range(n):
#                 if visited[i][j] ==0:
#                     path[0].append(maps[i][j])
#                 if visited[i][j] ==1:
#                     path[1].append(maps[i][j])
#
#         path[0].sort(reverse=True)
#         path[1].sort(reverse=True)
#         # print("path[0] : ",path[0])
#         # print("path[1] : ", path[1])
#
#
#         calc(0,path[0], 0, 0,[])
#         calc(1, path[1], 0, 0, [])
#         # print("test : ",test)
#
#
#         income = sum(list(map(lambda x : x**2,test[0]+test[1])))
#         # print("income : ",income)
#
#         ans = max(ans,income)
#         test = [[],[]]
#
#         return
#
#     for i in range(n):
#         for j in range(n):
#             if possible(i,j,visited):
#                 # print(f"i={i}, j={j},visited={visited}")
#                 adj_visited = set_visited(i,j,visited,cnt)
#                 dfs(i,j,cnt+1,adj_visited)
#                 visited = reset_visited(i,j,visited)

# tc = int(input())
# for case in range(1,tc+1):
#     n,m,c = map(int,input().split())
#     maps = [list(map(int,input().split())) for _ in range(n)]
#     ans = 0
#     test = [[],[]]
#     visited = [[-1]*n for _ in range(n)]
#     dfs(0,0,0,visited)
#     # calc(path[1], 0, 0,[])
#     # print("ans : ",ans)
#
#     print(f"#{case} {ans}")


# Best Code Review
import heapq

def dfs(n, cnt, sm, ci, cj):
    print(f"RTC x={ci},y={cj}, n={n}, cnt={cnt}, sm = {sm}")
    global mx
    if cnt > C:
        return
    if n == M:
        mx = max(mx, sm)
        return
    print(f"first x={ci},y={cj}, n={n}, data[x][y]={data[ci][cj]}, cnt={cnt}, sm = {sm}")
    dfs(n + 1, cnt, sm, ci, cj)
    print(f"second x={ci},y={cj}, n={n}, data[x][y+n]={cnt +data[ci][cj+n]}, cnt={cnt + data[ci][cj + n]}, sm = {sm + data[ci][cj + n] ** 2}")
    dfs(n + 1, cnt + data[ci][cj + n], sm + data[ci][cj + n] ** 2, ci, cj)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    mx = 0
    heap = []
    data = [list(map(int, input().split())) for _ in range(N)]
    mem = [[0 for _ in range(N)]  for _ in range(N)]
    for i in range(N):
        for j in range(N - M + 1):
            mx = 0
            dfs(0, 0, 0, i, j)
            mem[i][j] = mx

    print('mem : ', mem)
    for i in range(N):
        heapq.heappush(heap, -max(mem[i]))
    print("heapq : ", heap)
    print(f"#{test_case} {-(heapq.heappop(heap) + heapq.heappop(heap))}")