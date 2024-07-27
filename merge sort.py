'''
병합정렬 알고리즘

n개의 원소를 가진 배열을 재귀적으로 2분할 하면 O(logn)의 시간복잡도를 가짐
각 분할된 배열을 병합하는 과정에서 O(n)의 시간복잡도를 가짐
그래서 병합 정렬 전체의 시간 복잡도 O(nlogn)

idea : Devide and conquer (분할정복)
먼저 나눠서 정렬하고 합쳐보자!

'''

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide(분할): 리스트를 두 개의 부분 리스트로 분할합니다.
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Conquer(정복): 각 부분 리스트를 재귀적으로 정렬합니다.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Combine(결합): 정렬된 부분 리스트들을 병합하여 정렬된 리스트를 생성합니다.
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_idx = right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    # 남은 요소들을 병합합니다.
    merged += left[left_idx:]
    merged += right[right_idx:]

    return merged


# 예시 사용
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("정렬된 리스트:", sorted_arr)




