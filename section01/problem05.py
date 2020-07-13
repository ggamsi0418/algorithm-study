"""
1347. Minimum Number of Steps to Make Two Strings Anagram

https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
"""


class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        dict_s = {}
        dict_t = {}

        for word in s:
            dict_s[word] = dict_s.get(word, 0) + 1

        for word in t:
            dict_t[word] = dict_t.get(word, 0) + 1

        for index, value in dict_s.items():
            if index in t:
                if dict_s[index] <= dict_t[index]:
                    dict_t[index] -= dict_s[index]
                else:
                    dict_t[index] = 0

        return sum(dict_t.values())


sol = Solution()
print(sol.minSteps("bab", "aba"))
print(sol.minSteps("leetcode", "practice"))
print(sol.minSteps("anagram", "mangaar"))
