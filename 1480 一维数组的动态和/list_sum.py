class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret_list = []
        for i in range(len(nums)):
            ret_list.append(sum(nums[:i+1]))
        return ret_list
