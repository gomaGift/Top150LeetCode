from collections import Counter
from typing import List

'''
You are given a string s and an array of strings words. All the strings of words are of the same length.
A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.
For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings.
"acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.
'''


def find_sub_str(self, s: str, words: List[str]) -> List[int]:
    if not s or not words:
        return []

    result = []
    word_len = len(words[0])
    search_len = word_len * len(words)
    s_len = len(s)
    word_count = Counter(words)

    for i in range(word_len):
        left = right = i
        word_map = {}

        while right + word_len < s_len:
            word = s[right: right + word_len]

            if word in word_count:
                word_map[word] = word_map.get(word, 0) + 1

            if word_map[word] == word_count[word]:
                pass
            while word_map[word] > word_count[word]:
                word_map[left: left + word_len] -= 1
                left += word_len

            if (right - left) == search_len:
                result.append(left)

            else:
                word_map.clear()
                left = right
            right += word_len

