class Solution(object):
    def containsDuplicate(self, nums):
        sorted_s=sorted(nums)
        for i in range(1,len(sorted_s)):
            if sorted_s[i] == sorted_s[i-1]:
                return True
        return False

        