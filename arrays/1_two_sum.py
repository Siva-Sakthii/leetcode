class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i,v in enumerate(nums):
            complement = target-v
            if complement in d:
                return [d[complement],i]
            d[v] = i
        return