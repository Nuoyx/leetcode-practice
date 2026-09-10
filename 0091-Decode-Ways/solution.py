class Solution(object):

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        sLen = len(s)
        decodingList = [1] * (sLen + 1)
        for i in range(sLen-1, -1, -1):
            if s[i] == "0":
                decodingList[i] = 0
            else:
                decodingList[i] = decodingList[i+1]
                if i < sLen - 1:
                    if(s[i] == "1" or s[i:i + 2] < "27"):
                        decodingList[i] += decodingList[i+2]
        return decodingList[0]