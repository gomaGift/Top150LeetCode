from typing import List


def max_water(height: List[int]):
    
    max_area = float("-inf")
    left_ptr = 0
    right_ptr = len(height) - 1

    while left_ptr < right_ptr:
        length = min(height[left_ptr] , height[right_ptr])
        width = right_ptr - left_ptr
        water = length * width
        max_area = max(max_area, water)

        if length == height[left_ptr]:
            left_ptr +=1
        else:
            right_ptr -= 1

    return max_area


print(maxArea([1,8,6,2,5,4,8,3,7]))