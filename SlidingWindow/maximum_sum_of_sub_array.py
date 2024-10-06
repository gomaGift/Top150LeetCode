def maximum_sum_of_sub_array(arr: list[int], sub_array_size: int) -> int:
     
     low = 0
     high = sub_array_size - 1
     max_sum = float('-inf')
     while high < len(arr):
    
          curr_sum = sum(arr[low: high+1])
          max_sum = max(max_sum, curr_sum)
          low += 1
          high += 1
     return max_sum



print(maximum_sum_of_sub_array([2, 1, 5, 1, 3, 2], 3))

