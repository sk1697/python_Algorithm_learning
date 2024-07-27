'''
SWEA 2382
'''

from collections import deque,defaultdict
tc = int(input())
N,M,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(K)]


d = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs():
    q = deque()
    q.append([arr,0])

    while q:
        groups , time = q.popleft()

        for group in groups:

            dx =d[group[3]-1][0]
            dy = d[group[3]-1][1]
            nx = group[0] + dx
            ny = group[1] + dy
            if 0<= nx < N and 0<= ny <N:

                if nx ==0 or nx == N-1 and ny == 0 and ny ==N-1:
                    group[2] //= 2
                    if group[3] == 1:
                        group[3] = 2
                    elif group[3] == 2:
                        group[3] = 1
                    elif group[3] == 3:
                        group[3] = 4
                    else:
                        group[3] = 3
                group[0] = nx
                group[1] = ny

        check_dict = {}
        for g in groups:
            check_dict[f"{g[0]},{g[1]}"]=0
        for g in groups:
            check_dict[f"{g[0]},{g[1]}"] +=1

        print("check_dict", check_dict)
        print(f'time = {time} groups')
        for idx in range(len(groups)):
            print(*groups[idx])

        # print(f'time = {time} new_groups')
        # for i in range(len(new_groups)):
        #     print(*new_groups[i])

        if time < M:
            q.append([groups, time+1])

bfs()

