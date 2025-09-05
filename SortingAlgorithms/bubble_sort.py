from typing import List

def swap(to_sort, i, j):
    temp = to_sort[i]
    to_sort[i] = to_sort[j]
    to_sort[j] = temp


def bubble_sort(to_sort: List[int]):
    count = 0
    for i in range(len(to_sort)):
         count += 1
         for k in range(len(to_sort)-1, i, -1):
             if to_sort[k] < to_sort[k-1]:
                 swap(to_sort, k, k-1)
    print(count)
    return to_sort

# print(bubble_sort([1,2,3]))
#  complexity is 0(n^2)

def improved_bubble_sort(to_sort: List[int]):
    for i in range(len(to_sort)):
        swapped = 0
        for k in range(len(to_sort) - 1, i, -1):
            if to_sort[k] < to_sort[k-1]:
                swap(to_sort, k, k-1)
                swapped = 1
        if not swapped:
            return to_sort
    return to_sort

# print(improved_bubble_sort([1127, 220, 246, 277, 321, 454, 534, 565, 933]))
