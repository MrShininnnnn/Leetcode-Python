# -*- coding:utf-8 -*-
__author__ = 'Shining'

'''
Leetcode-Python-1.-Two Sum

1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        num_dict = {}
        for i in range(len(nums)):
            num_dict[nums[i]] = i
        
        for i in range(len(nums)):
            l = target - nums[i]
            try:
                if i != num_dict[l]:
                    return [i, num_dict[l]]
                else:
                    pass
            except:
                pass