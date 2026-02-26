class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        final_result = []

        # Fix the first element
        for i in range(0, n-2):  # Since second last and last element will be the second and third element
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = n-1

            needed = 0 - nums[i]

            while l < r:
                if nums[l] + nums[r] == needed:
                    each_result = [nums[i], nums[l], nums[r]]
                    final_result.append(each_result)

                    # Move both pointers
                    l += 1
                    r -= 1

                    # Skip duplicates for l
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

                    #Skip duplicates for r
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                elif nums[l] + nums[r] < needed:
                    l += 1
                else:
                    r -= 1
        return final_result
            
