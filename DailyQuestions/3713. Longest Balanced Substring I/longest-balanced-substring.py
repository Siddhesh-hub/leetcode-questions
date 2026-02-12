# Brute force + improvement (frequency array)
class Solution:
  def longestBalanced(self, s:str) -> int:
    n = len(s)
    ans =0
    for i in range(n):
      freq = [0]*26
      distinct = 0

      for j in range(i, n):
        idx = ord(s[j] - ord('a')
        freq[idx] += 1
        if freq[idx] == 1:
          distinct += 1

        # gather non-zero freq
        nonzero = [f for f in freq if f > 0]
        # Check if all are equal
        if len(nonzero) > 0 and len(set(nonzero) == 1:
          ans = max(ans, j - i + 1)
    return ans
