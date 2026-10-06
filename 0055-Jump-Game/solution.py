class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_pos = 0
        for i in range(len(nums)):
            if max_pos < i:
                return False
            if max_pos >= len(nums) - 1:
                return True
            max_pos = max(max_pos, i+nums[i])
        return False