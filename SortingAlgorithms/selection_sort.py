from typing import List

from SortingAlgorithms.bubble_sort import swap


def selection_sort(to_sort: List[int]):
    for i in range(len(to_sort)):
        least = i
        for j in range(i + 1, len(to_sort)):
            if to_sort[j] < to_sort[least]:
                swap(to_sort, j, i)
                least = j

    return to_sort

print(selection_sort([1127, 220, 246, 277, 321, 454, 534, 565, 933]))
