class Solution:
    def reverseBits(self, n: int) -> int:
        exp = 31
        num = 0
        while n > 0 and exp >= 0:
            if n & 1 == 1:
                num += 2 ** exp
            exp -= 1
            n = n >> 1
        return num