'''
SWEA 5644
'''
from itertools import combinations

case = int(input())
for tc in range(1,case+1):
    m,bc = map(int,input().split())
    mv_a = [0] + list(map(int,input().split()))
    mv_b = [0] + list(map(int,input().split()))
    bcs = [list(map(int,input().split())) for _ in range(bc)]

    # print("bcs : ",bcs)

    d = [(0,0),(-1,0),(0,1),(1,0),(0,-1)]

    arr = [[False]*10 for _ in range(10)]

    pos_a = [0,0] # A 시작위치
    pos_b = [9,9] # B 시작위치

    total = 0
    for i in range(m+1):
        dx1 ,dy1 = d[mv_a[i]]
        dx2, dy2 = d[mv_b[i]]

        # A의 다음 위치
        nx1 = pos_a[0] + dx1
        ny1 = pos_a[1] + dy1

        # B의 다음 위치
        nx2 = pos_b[0] + dx2
        ny2 = pos_b[1] + dy2

        ap_a ,ap_b,ab_sum = [] , [],[]
        for idx,bc in enumerate(bcs):
            a_flag = b_flag = False
            if abs(bc[1]-1-nx1) + abs(bc[0]-1-ny1) <= bc[2]:
                a_flag = True
                ap_a.append(idx)
            if abs(bc[1]-1 - nx2) + abs(bc[0]-1 - ny2) <= bc[2]:
                b_flag = True
                ap_b.append(idx)


        # print(f"#{i} ap_a : {ap_a}")
        # print(f"#{i} ap_b : {ap_b}")
        # print(f"#{i} combinations : {list(combinations(ap_a+ap_b,2))} ")
        if len(ap_a+ap_b)>0 and (len(ap_a) ==0 or len(ap_b)==0):
            if len(ap_a) == 0:
                for b in ap_b:
                    ab_sum.append(bcs[b][3])
            if len(ap_b) == 0:
                for a in ap_a:
                    ab_sum.append(bcs[a][3])
        else:

            for a in ap_a:
                for b in ap_b:
                    if a == b:
                        ab_sum.append(bcs[a][3])
                    else:
                        ab_sum.append(bcs[a][3]+bcs[b][3])


        # print(f"ab_sum : {ab_sum}")
        total+=max(ab_sum) if len(ab_sum)!=0 else 0
        pos_a[0] = nx1
        pos_a[1] = ny1

        pos_b[0] = nx2
        pos_b[1] = ny2
    print(f"#{tc} {total}")