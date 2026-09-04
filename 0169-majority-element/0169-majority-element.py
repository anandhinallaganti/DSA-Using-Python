class Solution(object):
    def majorityElement(self, nums):
        sorted_s = sorted(nums)
        return sorted_s[len(sorted_s)//2]

        

        