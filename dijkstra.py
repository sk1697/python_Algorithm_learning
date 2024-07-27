'''
Dijkstra algorithm

시간 복잡도 O(VlogV+E)

Idea : 한 노드에서 다른 모든 노드로의 최단경로 구하는 알고리즘

- 조건
1. 거리는 음수 가중치를 쓸 수 없음


'''

import heapq

def dijkstra(graph,start):
    # 거리 리스트 초기화
    distances = {node : float('infinity') for node in graph}
    # 출발점 초기화
    distances[start] = 0
    # print(distances)

    # heapq에 시작점 추가
    q = [(0,start)]

    while q:
        # print(q)
        # 매 순회마다 q에서 거리 및 노드 정보 꺼냄
        cdist ,cnode = heapq.heappop(q)

        # 현재 노드의 거리보다 계산된 노드의 거리보다 길다면 순회하지 않고 넘김
        if cdist > distances[cnode]:
            continue


        for nnode,ndist in graph[cnode].items():

            # print(ndist,nnode)
            new_dist = cdist+ndist

            # 새로 계산된 거리가 거리 리스트에 저장된것 보다 작으면 거리 갱신
            if new_dist < distances[nnode]:
                distances[nnode] = new_dist
                heapq.heappush(q,(new_dist,nnode))

    return distances

# 그래프 예제
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
short_dist = dijkstra(graph,'A')
print(short_dist)
