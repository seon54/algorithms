'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution:

    # From Discuss
    def twoSum1(self, nums, target):
        d = {}
        for i, n in enumerate(nums):    # enumerate (index, value) 반환
            m = target - n
            if m in d:      # d가 m이라는 key를 가지는지
                return [d[m], i]
            else:
                d[n] = i

    # Approach 1:Brute Forece
    # 시간복잡도: O(n^2), 공간복잡도: O(1)
    def twoSum2(self, nums, target):
        for i in range(len(nums)):            
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

    # Approach 2:Two-pass Hash Table
    # 시간복잡도: O(n), 공간복잡도: O(n)
    def twoSum3(self, nums, target):
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in d.keys() and d[complement] != i:
                return [i, d[complement]]

    # Approach 3:One-pass Hash Table
    # 시간복잡도: O(n), 공간복잡도: O(n)
    def twoSum4(nums, target):
        d = {}
        for i in range(len(nums)):
            print(d)
            complement = target - nums[i]
            if complement in d.keys():               
                return [d[complement], i]
            d[nums[i]] = i
