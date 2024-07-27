# A,B,C,D중에서 금,은,동메달 받을 사람 뽑는 경우의수

arr = [0,0,1,1,2,3,2,4,1,1,1] # br
path = [0]*len(arr)
used = [0]*len(arr) # br의 개수 만큼 만들기, 중복 방지위해 만듦

def abc(level):
    if level == len(arr):
        print(*path)
        return 
    for i in range(len(arr)):
        if used[i] == 0: # 중복 방지
            path[level]=arr[i]
            used[i] = 1
            abc(level+1)
            used[i] = 0 # 재귀 탈출하면 돌려줌
abc(0)