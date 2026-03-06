class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        counter = 1
        digits[len(digits) - counter] += 1
        while(True):
            index = len(digits) - counter
            if digits[index] == 10:
                if len(digits) == counter:
                    digits.insert(0, 1)
                    digits[index + 1] = 0
                    break
                else:
                    counter += 1
                    
                    digits[index - 1] += 1 
                    digits[index] = 0
            else:
                break
        return digits
        
        