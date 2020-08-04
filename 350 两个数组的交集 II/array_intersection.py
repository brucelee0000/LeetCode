class Solution(object):
    def intersect(self, nums1, nums2):
        """
        24 ms; 12.9 MB
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        list1 = list2 = 0
        res = []
        while list1 < len(nums1) and list2 < len(nums2):
            if nums1[list1] < nums2[list2]:
                list1 += 1
            elif nums1[list1] == nums2[list2]:
                res.append(nums1[list1])
                list1 += 1
                list2 += 1
            else:
                list2 += 1
        return res
