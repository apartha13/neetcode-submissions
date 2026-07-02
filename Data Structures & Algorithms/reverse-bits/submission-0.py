class Solution:
    def reverseBits(self, n: int) -> int:
        amount = 0
        for i in range(31, -1, -1):
            amount += (n & 1) * (2 ** i)
            n = n >> 1
        return amount

    """
        while n > 0:
            if n & 1 == 1:
                reverse.append(1)
            else:
                reverse.append(0)
            n = n >> 1
    """