class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        执行时间8896ms, 内存消耗15.4 MB
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        length_list = len(nums)
        large_num = None
        if length_list == k:
            return float(sum(nums)) / k

        for i in range(length_list-k+1):
            sub_list = nums[i:i+k]
            if i == 0:
                large_num = sum(sub_list)
                continue
            compare_num = sum(sub_list)
            if compare_num > large_num:
                large_num = compare_num
        return float(large_num) / k
