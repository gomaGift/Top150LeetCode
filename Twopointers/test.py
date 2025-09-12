# fruits = [1,2,2]
# try:
#     index = fruits.index(fruits[1], 2)
#     print(index)
# except ValueError:
#     print("Element not found in the list.")
from collections import Counter

t = "ABC"
s = "adobecodebanc"

print(s[0:5])
char_freq = Counter(t)

print(char_freq)
char_freq['A'] -= 1
print(char_freq)