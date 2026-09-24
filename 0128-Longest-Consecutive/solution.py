class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        num_set = set()
        for i in nums:
            num_set.add(i)

        longest_consecutive = 1
        curr_consecutive = 1

        for i in num_set:
            if (i-1) in num_set:
                continue
            curr = i
            while True:
                curr += 1
                if curr not in num_set:
                    break
                curr_consecutive += 1
            if curr_consecutive > longest_consecutive:
                longest_consecutive = curr_consecutive
            curr_consecutive = 1
            
        return longest_consecutive