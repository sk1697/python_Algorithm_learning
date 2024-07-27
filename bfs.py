# 1. 순열
from collections import deque

lst = [1, 2, 3]  # 주어진 원소
def bfs(lst, r):  # r은 주어진 원소 중 몇개를 나열 할껀지 정하는 argument
    q = deque()
    q.append([])  # 초기에 빈 리스트 입력

    while q:
        path = q.popleft()  # deque 자료형에서는 popleft 메서드로 가장 앞의 원소 출력

        if len(path) == r:
            print("permutations :", *path)  # path의 길이가 r개 경우만 출력

        for el in lst:  # 주어진 원소를 순회
            # path에 원소가 포함 하지 않으면 path에 추가(순열에는 순서의 개념이 있음)
            if el not in path:
                q.append(path + [el])

bfs(lst, 2)  # lst의 원소중 2개를 나열하는 모든 경우의 수 찾기



# 2. 조합
from collections import deque

lst = [1, 2, 3]
def bfs(lst, r):
    q = deque()
    q.append([])

    while q:
        path = q.popleft()

        if len(path) == r:  # path가 r 길이되면 path 출력
            print("combinations : ", *path)

        for el in lst:  # lst의 원소를 순회
            # path가 처음에 [] 임으로 lst의 각 원소를 큐에 추가하는 과정
            if len(path) == 0:
                q.append(path + [el])

            # 원소가 1개 이상일 때는, 큐의 마지막 원소 보다 큰 수가 포함되도록 구현
            if len(path) != 0 and path[-1] < el and el not in path:
                q.append(path + [el])

bfs(lst, 2)  # lst의 원소 중 순서 상관없이 2개를 뽑는 경우의 수

# 3. 중복 순열
from collections import deque

lst = [1, 2, 3]
def bfs(lst, r):
    q = deque()
    q.append([])

    while q:
        path = q.popleft()
        if len(path) == r:  # path의 길이가 r일 때, path 출력
            print("duplicate Permutations : ", *path)

        for el in lst:
            # 순열과 다르게 path에 el 원소가 포함하지 않게 하는 조건을 빼고
            # q 에 원소를 무한 삽입을 방지하기 위해 r개 이하에서만 원소 삽입하게 조건 추가
            if len(path) < r:
                q.append(path + [el])

bfs(lst, 2)  # lst 원소 중 2개를 중복 가능하게 선택하여 나열하는 경우의 수


# 4. 중복 조합
from collections import deque

lst = [1, 2, 3]
def bfs(lst, r):
    q = deque()
    q.append([])

    while q:
        path = q.popleft()
        if len(path) == r:  # path의 길이가 r일때 , path 출력
            print("duplicate Combinations : ", *path)

        for el in lst:
            # 초기 path에 []이므로 , lst 각 원소를 추가하는 과정
            if len(path) == 0:
                q.append(path + [el])

            # path의 길이가 1이상일 때, path의 마지막 원소가 순회하는 원소와 같은 수 이상일 때만 추가
            # q의 삽입이 무한 반복을 방지하기 위해 r이하일 때만 q에 추가하도록 구현
            if 0 < len(path) < r and path[-1] <= el:
                q.append(path + [el])

bfs(lst, 2)  # lst 원소 중 2개를 중복 가능하게 뽑는 경우의 수