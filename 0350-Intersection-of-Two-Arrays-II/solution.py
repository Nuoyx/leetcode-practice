class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dup = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        nums1_index = 0
        nums2_index = 0
        while(True):
            if nums1_index >= len(nums1):
                break
            if nums2_index >= len(nums2):
                break
            if nums1[nums1_index] < nums2[nums2_index]:
                nums1_index += 1
            elif nums2[nums2_index] < nums1[nums1_index]:
                nums2_index += 1
            else:
                dup.append(nums1[nums1_index])
                nums1_index += 1
                nums2_index += 1
        return dup