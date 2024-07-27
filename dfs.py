# 1. 순열

lst = [1, 2, 3]  # 주어진 원소
visited = [False] *len(lst)
r = 2
def dfs(path):
    # print("visited : ", visited)
    if len(path) == r:
        print("permutations : ", *path)
        return

    for i in range(len(lst)):
        if not visited[i]:
            visited[i] = True
            path.append(lst[i])
            dfs(path)
            visited[i] = False
            path.pop()
dfs([])

# 2. 조합
lst = [1, 2, 3]  # 주어진 원소
r = 2
def dfs(path,el):
    # print("visited : ", visited)
    if len(path) == r:
        print("combinations : ", path)
        return

    for i in range(el,len(lst)):
        if not visited[i]:
            visited[i] = True
            path.append(lst[i])
            dfs(path,i)
            visited[i] = False
            path.pop()
dfs([],0)

# 3. 중복 순열

lst = [1, 2, 3]  # 주어진 원소
r = 2
def dfs(path):
    # print("visited : ", visited)
    if len(path) == r:
        print("duplicate permutations : ", *path)
        return

    for i in range(len(lst)):

            path.append(lst[i])
            dfs(path)
            path.pop()
dfs([])

# 4. 중복 조합
lst = [1, 2, 3]  # 주어진 원소
r = 2
def dfs(path,el):
    # print("visited : ", visited)
    if len(path) == r:
        print("duplicate combinations : ", *path)
        return

    for i in range(el,len(lst)):
        path.append(lst[i])
        dfs(path,i)
        path.pop()
dfs([],0)