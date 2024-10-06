from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
        nums.sort()
        left = 0, right = 0
        commulative_sum = 0
        minSize = float('inf')


        while right < len(nums):
                  commulative_sum += nums[right]
                  if commulative_sum > target:
                          while commulative_sum > target:
                            commulative_sum -= nums[left]
                            left += 1
                  elif commulative_sum < target:
                          right += 1
                  else:
                        minSize = min(right - left +1, minSize)
                        right += 1
                  
                        
                          
                
                        