class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x

        # 查找区间为[1, x//2 + 1)
        left = 1
        right = x//2 + 1
        while left < right:
            mid = (left + right) // 2
            square = mid * mid
            if square > x:
                right = mid
            else:
                left = mid + 1
        return left - 1
