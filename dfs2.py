def dfs(arr, idx, elements, result):
    if idx == len(arr):
        result.append(arr[:])  # 현재 상태를 결과에 추가
        return

    for elem, length in elements.items():
        if idx + length <= len(arr):
            arr[idx:idx+length] = [elem] * length  # 현재 위치부터 길이만큼 요소 할당
            dfs(arr, idx + length, elements, result)  # 다음 위치로 이동하여 재귀적으로 탐색

# 초기 설정
arr = [''] * 50  # 50개의 공간을 가진 배열
elements = {'a': 2, 'b': 3, 'c': 2}  # 요소 및 길이 설정
result = []  # 결과를 저장할 리스트

# DFS 호출
dfs(arr, 0, elements, result)

# 결과 출력
for combination in result:
    print(combination)
