# itertools 순열 연습
from itertools import permutations
import time
# 6개의 요소를 가진 순열
# arr = [0,1,1,2,2,3]
arr = range(50)
start = time.time()
for idx,case in enumerate(permutations(arr,len(arr))):
    print(idx,case)

print(time.time() - start)