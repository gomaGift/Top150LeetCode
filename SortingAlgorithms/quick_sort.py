from random import random, Random
from typing import List
from bubble_sort import swap


def quick_sort(to_sort: List[int], low: int, high: int):
    if low < high:
        pivot = partition(to_sort, low, high)
        quick_sort(to_sort, low, pivot - 1)
        quick_sort(to_sort, pivot + 1, high)


def partition(to_sort: List[int], low: int, high: int):
    pivot = low
    swap(to_sort, pivot, high)
    for i in range(low, high):
        if to_sort[i] <= to_sort[high]:
            swap(to_sort, i, low)
            low += 1

    swap(to_sort, low, high)
    return low


to_sort = [1127, 220, 246, 277, 321, 454, 534, 565, 933]
quick_sort(to_sort, 0, len(to_sort) - 1)
print(to_sort)


def randomized_partition(unsorted: List[int], low: int, high: int):
    pivot = random()
