'''
SWEA 5658
'''

tc = int(input())
for case in range(1, tc + 1):
    n, k = map(int, input().split())
    arr = list(map(str, input()))

    # print("arr : ",arr)

    len_num = int(n / 4)

    initial_arr = []
    ans_set = set()
    for j in range(0, n - len_num, len_num):
        initial_arr.append(''.join(arr[j:j + len_num]))
    # print(f"initial_arr : ", initial_arr)
    ans_set.update(initial_arr)

    for shift in range(1, len_num + 1):
        shift_arr = []
        temp = []
        for i in range(n):
            # print(f"before : ",arr[(j) % n])
            # print(f"shift : ",(arr[(j+shift)%n]))
            temp.append(arr[(i - shift) % n])
        # print(f"before : ", arr)
        # print(f"shift : ", temp)
        for j in range(0, n - len_num + 1, len_num):
            shift_arr.append(''.join(temp[j:j + len_num]))
        # print(f"shift_arr : ", shift_arr)
        ans_set.update(shift_arr)

    # print("ans_set : ",ans_set)
    ans_set = sorted(list(ans_set), key=lambda x: int(x, 16), reverse=True)
    # print("sorted ans_set : ",ans_set)
    print(f"#{case} {int(ans_set[k - 1], 16)} ")