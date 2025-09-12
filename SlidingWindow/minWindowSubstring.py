from collections import Counter
def min_window_sub_string(s, t):
    if s == t:
        return t
    min_str = ""
    min_len = float("inf")
    if len(t) > len(s):
       return min_str

    left = right = 0
    formed = 0
    char_freq = Counter(t)
    required = len(char_freq)
    char_map = {}
    while right < len(s):
        char = s[right]
        char_map[char] = char_map.get(char, 0) + 1
        if char in char_freq and char_map[char] == char_freq[char]:
            formed += 1
        while formed == required and left <= right:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_str = s[left: right+1]
            left_char = s[left]
            char_map[left_char] -= 1
            if left_char in char_freq and char_map[left_char] < char_freq[left_char]:
                formed-=1
            left += 1
        right += 1
    return min_str


print(min_window_sub_string("ADOBECODEBANC", "ABC"))