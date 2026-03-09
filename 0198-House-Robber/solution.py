class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = 0
        prev_max = 0
        for num in nums:
            temp = max(prev_max, prev + num)
            prev = prev_max
            prev_max = temp
        return prev_max