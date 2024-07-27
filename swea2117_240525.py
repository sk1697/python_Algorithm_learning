'''
SWEA 2117
'''
from collections import deque
tc = int(input())
for case in range(1,tc+1):
    n,m = map(int,input().split())
    graph = [list(map(int,input().split())) for i in range(n)]

    house_list = set()
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                house_list.add((i,j))

    # print(house_list)
    ans = 0
    for k in range(1,n+2):
        # print(f"k = {k}일 때")
        cost = k*k + (k-1)*(k-1)

        for x in range(n):
            for y in range(n):
                # print(f"x={x}, y={y}, cost={cost}")
                cnt = 0
                # x,y 위치에서 k 범위의 house check
                for hx, hy in house_list:
                    if abs(hx-x) + abs(hy-y) <k:
                        # print(f"hx={hx}, hy={hy}, cnt={cnt}")
                        cnt+=1

                # print("여기서 cnt : ",cnt)
                if cost <= cnt * m:
                    # print(f"x={x}, y={y}, cost={cost}")
                    # print("cnt :", cnt)
                    ans = max(ans,cnt)

    print(f"#{case} {ans}")

