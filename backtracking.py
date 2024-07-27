# 백트래킹 기본

# 1. 일반순열 (4개 중에 3개 나열)

arr = ['A','B','C','D']
visited = [False]*4
path = []

def bt(cnt):
    if cnt == 3:
        print(*path)
        return # 종료 조건

    for i in range(4):
        if not visited[i]: #진입 전에 특정 조건으로 제외 가능
            visited[i] = True
            path.append(arr[i])
            bt(cnt+1)
            visited[i] = False
            path.pop()
# bt(0)

# 2. 특정 조건이 붙은 경우 순열 ABCD중에 C로 시작하는 경우 제외 순열
path =[]
visited= [False]*4
def bt1(cnt):
    if cnt ==3:
        print(*path)

    for i in range(4):
        if arr[i] == "C" and cnt==0: continue
        if not visited[i]:
            visited[i] = True
            path.append(arr[i])
            bt1(cnt+1)
            visited[i] = False
            path.pop()
# bt1(0)

# 3. ABCD 중 3개 중복 순열
path = []
def bt2(cnt):
    if cnt == 3:
        print(*path)
        return

    for i in range(4):
        # print(i,arr[i])
        path.append(arr[i])
        bt2(cnt+1)
        path.pop()
# bt2(0)

# 4. ABCD 중 3개 B는 모든 경우에서 제외, 3개 중복 조합
path = []

def bt3(cnt):
    if cnt == 3:
        print(*path)
        return

    for i in range(4):
        if i ==1: continue # B의 인덱스가 1인 경우는 진입 전에 제외
        path.append(arr[i])
        bt3(cnt+1)
        path.pop()
bt3(0)

# BOJ N Queen 문제

n = int(input())

abs = 0
row = [0]*n
def is_promising(x):
    for i in range(x):
        if row[x]== row[i] or abs(row[x] - row[i]) == abs(x-i): # 대각선과 현재 위치 하는 열 전에 행에서 퀸이 위치 하는지 확인
            return False

    return True

def n_queens(x):
    global ans
    if x == n: #체스판 끝까지 도달했다면, 정답인 케이스
        ans +=1
        return

    else:
        for i in range(n):
            row[x] = i # row x행에 i 번째 열에 퀸을 놓겠다.
            if is_promising(x): # 퀸이 있을수 있는지 가능성 따져보고, x+1행으로 들어가서 다시 확인
                n_queens(x+1)