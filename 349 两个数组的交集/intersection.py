class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        ret_list = []
        for each in set1:
            if each in set2:
                ret_list.append(each)
        return ret_list
