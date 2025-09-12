from typing import List


def min_sub_array_sum(target: int, nums: List[int]) -> int:
       left = right = 0
       total_sum = 0
       min_len = float("inf")
       while right < len(nums):
           total_sum += nums[right]
           while total_sum >= target and left <= right:
               min_len = min(min_len, right - left + 1)
               total_sum -= nums[left]
               left += 1
           right += 1
       return 0 if min_len == "inf" else min_len


print(min_sub_array_sum(213, [12,28,83,4,25,26,25,2,25,25,25,12]))

                  
                        
                          
                
                        