# Brute force implementation
class Solution:

    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        longest_subarray_length = 0
        for i in range(0, n):
            even_set = set()
            odd_set = set()
            for j in range(i, n):
                if nums[j]%2==0:
                    even_set.add(nums[j])
                else:
                    odd_set.add(nums[j])
                if len(even_set) == len(odd_set) and longest_subarray_length< len(nums[i:j+1]):
                    longest_subarray_length = len(nums[i:j+1])
        return longest_subarray_length
