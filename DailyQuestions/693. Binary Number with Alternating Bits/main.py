class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_n = bin(n)[2:]
        len_n = len(bin_n)
        for i in range(1, len_n):
            if bin_n[i]==bin_n[i-1]:
                return False
        return True
