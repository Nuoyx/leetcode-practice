class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        first = strs[0]
        last = strs[-1]
        length = 0;

        for i in range(len(first)):
            if first[i] == last[i]:
                length += 1
            else:
                break
        return first[:length]