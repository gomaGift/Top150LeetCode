from typing import List


def find_max_sub_average(nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        max_sum = curr_sum

        for i in range(k, len(nums)):
            curr_sum = curr_sum + nums[i] - nums[i-k]
            if curr_sum > max_sum:
                max_sum = curr_sum


        return max_sum / float(k)
    
print("answ",find_max_sub_average([1,12,-5,-6,50,3], 4))