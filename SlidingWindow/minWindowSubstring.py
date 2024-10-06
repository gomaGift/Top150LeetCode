from typing import Counter


def minWindow(self, s: str, t: str) -> str:
        windowCount = {}
        tCharFrequency = Counter(t)
        required = len(tCharFrequency)
        left, right = 0, 0
        ans = float('inf'), None, None
        formed = 0
        while right < len(s):
            char = s[right]
            windowCount[char] = windowCount.get(char, 0) + 1
            if char in tCharFrequency and tCharFrequency[char] == windowCount[char]:
                formed += 1
            
            while left <= right and formed == required:
                 char = s[left]
                 
                 if right - left + 1 < ans[0]:
                      ans = (right - left + 1, left, right)

                 windowCount[char] -= 1
                 if char in tCharFrequency and tCharFrequency[char] > windowCount[char]:
                      formed -= 1

                 left += 1

            right += 1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

                
            

