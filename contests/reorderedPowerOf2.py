class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        digits = []

        if N == 1:
            return True

        while N > 0:
            digits.append(N % 10)
            N = N / 10

        digits.sort()

        for i in range(36):
            if self.toSortedArray(1 << i) == digits:
                return True

        return False

    def toSortedArray(self, n):
        nn = []
        while n > 0:
            nn.append(n % 10)
            n = n / 10
        return sorted(nn)

s = Solution().reorderedPowerOf2(2048)
print s