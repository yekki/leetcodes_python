#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n1 in range(len(nums)):
            for n2 in range(len(nums)):
                if n1 != n2:
                    if nums[n1] + nums[n2] == target:
                        return [nums[n1], nums[n2]]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    s = Solution()
    print(s.twoSum(nums, 9))
