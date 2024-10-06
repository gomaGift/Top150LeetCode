from typing import List


def bubbleSort(arr: List[int]) -> List[int]:
    passes = len(arr) - 1
    for i in range(passes):
        flag = 0
        for j in range(passes - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                flag = 1
        if not flag:
            return arr
        

print(bubbleSort([1,10,-200, 3,4]))