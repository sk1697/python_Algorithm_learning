'''
SWEA 2477

bfs 사용하여 각 상태관리를 시간마다 업데이트하여 구현
'''

from collections import deque
tc = int(input())
for case in range(1,tc+1):
    N,M,K,A,B = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    t = deque(list(map(int,input().split())))


    # 접수 창구 세팅
    recept = {i : deque() for i in range(1,N+1)}
    # print({i : deque() for i in range(1,N+2)})

    # 정비 창구 세팅
    repair = {i : deque() for i in range(1,M+1)}

    # 접수/정비 wait 세팅
    recept_wait = deque()
    repair_wait = deque()
    result = deque()
    customer = 0

    q = deque()
    q.append([0, recept_wait,recept,repair_wait, repair, result])

    while q:
        time, recept_wait,recept,repair_wait, repair, result = q.popleft()

        # 고객 도착시간에 맞춰 recept wait에 할당
        while t:
            recept_wait_flag = False
            if t[0] ==time:
                t.popleft()
                customer +=1
                recept_wait.append(customer)
                recept_wait_flag = True

            if not recept_wait_flag:
                break



        # 접수 창구 할당
        for recept_num in recept.keys():
            if recept[recept_num]:
                if recept[recept_num][0][2] == 0:
                    repair_wait.append([*list(recept[recept_num].popleft())[:-1]])
                else:
                    recept[recept_num][0][2]-=1

            if not recept[recept_num] and recept_wait:
                recept[recept_num].append([recept_wait.popleft(),recept_num,a[recept_num-1]-1])

        # 정비 창구 wait 할당
        for repair_num in repair.keys():
            if repair[repair_num]:
                if repair[repair_num][0][3] == 0:
                    result.append([*list(repair[repair_num].popleft())])
                else:
                    repair[repair_num][0][3]-=1

            if not repair[repair_num] and repair_wait:
                repair[repair_num].append([*list(repair_wait.popleft()), repair_num, b[repair_num - 1] - 1])

        # print(f"time={time}")
        # print(f"recept_wait={recept_wait}, recept={recept}")
        # print(f"repair_wait={repair_wait}, repair={repair}")
        # print(f"result={result}")

        if len(result) < K :
            q.append([time+1, recept_wait,recept,repair_wait, repair, result ])
    ans = sum(list(map(lambda x : x[0],list(filter(lambda x : (x[1]==A)and(x[2]==B),result)))))
    ans = -1 if ans ==0 else ans
    print(f'#{case} {ans}')















