class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for chr in s:
            if s.rindex(chr) == s.index(chr):
                return s.index(chr)
        return -1
        
        