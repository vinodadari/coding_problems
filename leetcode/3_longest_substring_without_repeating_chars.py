"""
3. Longest Substring Without Repeating Characters

    Given a string s, find the length of the longest substring without repeating characters.


Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

TestCases
"abcabcbb" - 3
"bbbbb" - 1
"pwwkew" - 3
" " - 1
"au" - 2
"ckilbkd" - 5
"dvdf" - 3
"abcdbcd"
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lower_bound = 0
        upper_bound = 5 * 10**4
        string_len = len(s)
        substrings = [0]
        temp_substring = ""

        if string_len == 1:
            return 1

        if lower_bound <= string_len <= upper_bound:
            for str_index in range(string_len):
                next_str = s[str_index]
                if next_str in temp_substring:
                    last_occurrence = temp_substring.rfind(next_str)
                    substrings.append(len(temp_substring))
                    temp_substring = temp_substring[last_occurrence + 1:]
                temp_substring += next_str

            substrings.append(len(temp_substring))

        return max(substrings)


# optimized codes

# chat GPT
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_len = len(s)
        if string_len == 0:
            return 0

        char_index_map = {}
        max_length = 0
        start_index = 0

        for end_index in range(string_len):
            if s[end_index] in char_index_map and char_index_map[s[end_index]] >= start_index:
                start_index = char_index_map[s[end_index]] + 1

            char_index_map[s[end_index]] = end_index
            max_length = max(max_length, end_index - start_index + 1)

        return max_length

