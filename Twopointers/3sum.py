

# return a list of triplets whose sum equal zero

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:

    triplets = []
    nums.sort()
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        target = -nums[i]
        ptr_1 = i + 1
        ptr_2 = len(nums) - 1
        while ptr_1 < ptr_2:
            sum = nums[ptr_1] + nums[ptr_2]

            if sum == target:
                triplets.append([nums[i], nums[ptr_1], nums[ptr_2]])

                while ptr_1 < ptr_2 and nums[ptr_1] == nums[ptr_1 + 1]:
                        ptr_1 += 1
                
                while ptr_1 < ptr_2 and nums[ptr_2] == nums[ptr_2 - 1]:
                         ptr_2 -= 1

                ptr_1 += 1
                ptr_2 -= 1

            elif sum > target:
                ptr_2 -= 1 
            
            else:
                 ptr_1 += 1

    return triplets


             
print(three_sum([-1, 0, 1, 2, -1, -4]))