'''

Strong Connected Components (SCC) 강한연결요소

시간 복잡도 ?

Idea : cycle있는 무향 그래프에서는 의미가 없고 DAG(Directed Acyclic Graph)에서는 방향이
시작 노드로 돌아가는 경우 순환을 판단하고 이때 SCC 관계에 있다고 함

구현 알고리즘 : 코사라주 알고리즘과 타잔 알고리즘이 있음

타잔알고리즘 구현 시
O(V+E) 시간복잡도

6 7
1 2
2 3
3 1
3 4
3 6
4 5
5 4
'''
import collections
v,e = map(int,input().split())  # 정점과 간선 입력받기

graph = collections.defaultdict(list) # 그래프는 dictionary 타입으로 자료형 만듬

# DAG 그래프 인접리스트 만들기
for _ in range(e):
    # 간선정보 입력받기
    a , b = map(int,input().split())
    graph[a-1].append(b-1)

print("Graph : ",graph)
d = [-1 for _ in range(v)] # 방문 체크 및 부모 번호 리스트
stack = [] # node 정보 담는 자료형
on_stack = [False for _ in range(v)] # scc 확인용 체크
id = 0 # 부모 노드 id 관리

def scc(cur):
    print("=" * 40)
    print("cur  : ",cur)
    global id
    id+=1
    d[cur] = id
    stack.append(cur)
    on_stack[cur] = True
    print("id : ",id)
    print("d : ",d)
    print("on_stack",on_stack)
    print("stack",stack)

    parent = d[cur]
    # 하위 노드에서 부모 id 업데이트 과정
    for next in graph[cur]:

        print("next : ", next)
        print("d[next] : ", d[next])
        print("on_stack[next] : ", on_stack[next])
        print("parent : ", parent)

        if d[next] == -1: # 방문한적이 없는 노드라면,

            parent = min(parent,scc(next))
        elif on_stack[next]: # 방문은 했지만 아직 처리 안됨

            parent = min(parent,d[next])

    #scc result
    print(f"parent / d[cur] : {parent} / {d[cur]}")
    print("on_stack : ", on_stack)
    if parent == d[cur]:
        scc_subset = []
        while True:
            node = stack.pop()
            on_stack[node] = False
            print("node : ", node)
            scc_subset.append(node+1) #node는 0부터 되고 실제숫자는 +1 해줘야됨
            if cur == node:
                break
        print("Strongly Connected Component", *scc_subset)

    return parent

for i in range(v):
    if d[i]==-1: #방문 이력이 없는 노드
        scc(i)














