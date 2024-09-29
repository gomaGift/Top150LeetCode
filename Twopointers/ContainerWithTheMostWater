from typing import List


def maxArea(height: List[int]):
    
    max_water = -1
    min_ptr = 0
    max_ptr = len(height) - 1

    while min_ptr < max_ptr:
        length = min(height[min_ptr] , height[max_ptr])
        width = max_ptr - min_ptr
        water = length * width
        max_water = max(max_water, water)

        if length == height[min_ptr]:
            min_ptr += 1
        else:
            max_ptr -= 1

    return max_water


print(maxArea([1,8,6,2,5,4,8,3,7]))