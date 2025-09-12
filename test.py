from random import random
from typing import List


def to_binary(n, bits=8):
    return format((n + (1 << bits)) % (1 << bits), f'0{bits}b')

print(to_binary(-8, 11))   # 11111011
print(to_binary(-12, 11))  # 1111111111111011
print(to_binary(-20, 11))
print("11111101100")


nums = [2,3,1,5]
nums.sort()

# set
output = set()
output.add((2,3))
nums = list(output)
print(nums)

height = float("-inf")
print(height)

print(nums)