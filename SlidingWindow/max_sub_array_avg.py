from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0] / k
        

        low = 0
        high = k-1
        max_avg = float('-inf')
        while high < len(nums):
            curr_sum = sum(nums[low: high+1])
            max_avg = max(max_avg, curr_sum / k)
            
            low += 1
            high += 1
        return max_avg
    
print(findMaxAverage([1,12,-5,-6,50,3], 4))