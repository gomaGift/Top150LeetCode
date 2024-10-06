from typing import List


def insertionSOrt(arr: List[int]) -> List:
    if len(arr) == 0 or len(arr) == 1:
        return arr
    
    
    for i in range(1, len(arr)):
        
        while arr[i] < arr[i - 1]:
            temp = arr[i]
            arr[i] = arr[i-1]
            arr[i-1] = temp
            
        
        
    return arr


print(insertionSOrt([1,10,-200, 3,4]))
