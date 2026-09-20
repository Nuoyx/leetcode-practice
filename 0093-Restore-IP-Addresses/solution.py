class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4 or len(s) > 12:
            return []

        return self.restoreHelper(s)

    def restoreHelper(self, s):
        result = []

        for i in range(1, 4):
            part1 = s[:i]
            if i + 3 > len(s) or not self.valid(part1):
                continue
            for j in range(1, 4):
                part2 = s[i:i + j]
                if i + j + 2 > len(s) or not self.valid(part2):
                    continue

                for k in range(1, 4):
                    part3 = s[i + j:i + j + k]
                    if i + j + k + 1 > len(s) or not self.valid(part3):
                        continue

                    for l in range(1, 4):
                        if i + j + k + l != len(s):
                            continue
                        part4 = s[i + j + k:i + j + k + l]

                        if self.valid(part4):
                            ip = part1 + "." + part2 + "." + part3 + "." + part4
                            result.append(ip)
        return result

    def valid(self, s):
        if len(s) > 1 and s[0] == "0":
            return False
        return int(s) <= 255