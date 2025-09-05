from typing import List


def merge_sort(to_sort: List[int]):
    if len(to_sort) > 1:
        mid = len(to_sort) // 2
        left = to_sort[:mid]
        right = to_sort[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                to_sort[k] = left[i]
                i+=1
            else:
                to_sort[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            to_sort[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            to_sort[k] = right[j]
            j+=1
            k+=1

a = [1127, 220, 246, 277, 1, 454, 534, 565, 933]
merge_sort(a)
print(a)
