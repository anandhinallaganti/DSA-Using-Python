class Solution(object):
    def productExceptSelf(self, nums):
        x=1
        n=len(nums)
        a=[1]*n
        for i in range(n):
            a[i]=x
            x=x*nums[i]
        y=1
        for i in range(n-1,-1,-1):
            a[i]*=y
            y*=nums[i]
        return a

        