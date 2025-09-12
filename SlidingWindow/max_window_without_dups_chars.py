def max_window_without_repeating_chars(s: str):
    max_len = 0
    char_map = {}
    left = 0
    for right in range(len(s)):
        char = s[right]
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        char_map[char] = right
        max_len= max(max_len, right - left +1)

    return  max_len

print(max_window_without_repeating_chars("abcabcbb"))