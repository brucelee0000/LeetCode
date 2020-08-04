class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        以初始k个数的和为基准，记录后续和的变化(812ms 15.5MB)
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        delt = 0
        deltsum = 0
        maxdelt = -20000
        for i in range(len(nums) - k):
            delt = nums[i + k] - nums[i]
            deltsum += delt
            if deltsum > maxdelt:
                maxdelt = deltsum
        if maxdelt <= 0:
            return sum(nums[:k]) / float(k)
        else:
            return (sum(nums[:k]) + maxdelt) / float(k)
