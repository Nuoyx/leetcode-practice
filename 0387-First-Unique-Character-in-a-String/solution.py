class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev = set()
        for i in range(len(s)):
            c = s[i]
            if c not in prev:
                if c not in s[i+1:]:
                    return i
                else:
                    prev.add(c)
        return -1