from typing import List


def insertion_sort(to_sort: List[int]):
    for i in range(1, len(to_sort)):
        while  i > 0 and to_sort[i] < to_sort[i-1]:
            temp = to_sort[i]
            to_sort[i] = to_sort[i-1]
            to_sort[i-1] = temp
            i-= 1
            print(i)
    return to_sort


print(insertion_sort([1127, 220, 246, 277, 1, 454, 534, 565, 933]))
