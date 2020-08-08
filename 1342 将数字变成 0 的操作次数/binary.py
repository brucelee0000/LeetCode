class Solution:
    def numberOfSteps (self, num: int) -> int:
        """
        len(binary)是计算除2的次数，但需要实际的二进制长度减1，有符号两位,最后减1+2=3
        count("1")是看减一次数
        :param num:
        :return:
        """
        binary = bin(num)
        return len(binary) + binary.count("1") - 3
