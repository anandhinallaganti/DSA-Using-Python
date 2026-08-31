class Solution(object):
    def twoSum(self, nums, target):
       new = {}
       for i,num in enumerate(nums):
        complement = target - num
        if complement in new:
            return [new[complement],i]
        new[num]=i
       return []
        