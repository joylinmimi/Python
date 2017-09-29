class Solution(object):
    def twoSum(self, nums, target):
        i=0
        n=len(nums)
        while i <= (n-1):
            j=i+1
            while j <=(n-1):
                if nums[i]+nums[j] != target:
                    j=j+1
                else:
                    return[i,j]
            i=i+1
                
            