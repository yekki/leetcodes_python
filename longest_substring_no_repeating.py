#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 1 if len(s) == 1 else 0

        for i, c in enumerate(s):
            cset = set()

            for j, jc in enumerate(s[i:]):
                cset.add(jc)

                if len(cset) != j + 1:
                    if max_len < j: max_len = j
                    break
                else:
                    if max_len < len(cset): max_len = len(cset)
        return max_len


if __name__ == '__main__':
    solution = Solution()
    # for j in range(1, 3):
    #     print(j)
    print(solution.lengthOfLongestSubstring('au'))
