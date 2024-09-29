from typing import List


def two_sum(numbers: List[int], target: int ) -> List[int]:   
       
       output = []
       ptr_1 = 0
       ptr_2 = len(numbers) - 1

       while ptr_1 < ptr_2:
              sum = numbers[ptr_1] + numbers[ptr_2]
              if sum == target:
                     output.append(ptr_1 + 1)
                     output.append(ptr_2+1)
                     return output

              if sum > target:
                     ptr_2 -= 1
              else:
                     ptr_1 += 1
       return output



print(two_sum([2,7,11,15], 9))
