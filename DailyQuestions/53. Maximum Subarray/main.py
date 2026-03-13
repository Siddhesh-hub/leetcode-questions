# Solution using Kadanes algorithm

# ===========================================================
# Working optimized solution with highest runtime - 46 ms
# ===========================================================
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         subarray_sum=nums[0]
#         curr_sum=nums[0]
#         n = len(nums)
#         for i in range(1,n):
#             curr_sum = max(curr_sum+nums[i], nums[i])
#             subarray_sum=max(subarray_sum, curr_sum)
#         return subarray_sum


# ===========================================================
# Working optimized solution with optimized runtime - 35 ms
# ===========================================================
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         subarray_sum= curr_sum =nums[0]
#         for i in nums[1:]:
#             curr_sum = max(curr_sum+i, i)
#             subarray_sum=max(subarray_sum, curr_sum)
#         return subarray_sum


# ===========================================================
# Working optimized solution with best runtime - 19 ms
# ===========================================================
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subarray_sum= curr_sum =nums[0]
        for i in nums[1:]:
            # curr_sum = max(curr_sum+i, i)
            if curr_sum < 0 :
                curr_sum = i
            else:
                curr_sum += i
            
            # subarray_sum=max(subarray_sum, curr_sum)
            if subarray_sum > curr_sum:
                subarray_sum = subarray_sum
            else:
                subarray_sum = curr_sum
        return subarray_sum
