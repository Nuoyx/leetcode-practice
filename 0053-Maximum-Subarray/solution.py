class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = nums[0]
        temp_max = max
        for i in range(1, len(nums)):
            if temp_max <= 0:
                temp_max = nums[i]
            else:
                temp_max += nums[i]
            if temp_max > max:
                max = temp_max
        return max
