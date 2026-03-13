# 53. Maximum Subarray

## 📌 Problem

Given an integer array `nums`, find the **contiguous subarray** (containing at least one number) which has the **largest sum**, and return its sum.

A **subarray** is a **contiguous part of the array**.

---

## 🧾 Examples

### Example 1
Input:
nums = [-2,1,-3,4,-1,2,1,-5,4]

Output:
6

Explanation:
The subarray [4,-1,2,1] has the largest sum = 6


### Example 2
Input:
nums = [1]

Output:
1


### Example 3
Input:
nums = [5,4,-1,7,8]

Output:
23

---

## 🔒 Constraints

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

---

# 🧠 Key Insight

At every element we must decide:

1. Extend the current subarray
2. Start a new subarray from the current element

If the **running sum becomes negative**, continuing it will only **reduce the future sum**.

Therefore:

Restart the subarray whenever the running sum becomes negative.

This idea leads to **Kadane's Algorithm**.

---

# 📊 Solution Evolution (Least → Most Optimized)

We will go through **three versions** of the same algorithm improving **clarity and micro-optimization**.

All solutions run in:

Time Complexity: **O(n)**  
Space Complexity: **O(1)**

---

# 🥉 Solution 1 — Standard Kadane (Using max())

## Idea

At each element:

curr_sum = max(curr_sum + current_element, current_element)

Meaning:

- Either extend the previous subarray
- Or start a new subarray from the current element

Then update the global maximum.

---

## Code

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subarray_sum = curr_sum = nums[0]

        for i in nums[1:]:
            curr_sum = max(curr_sum + i, i)
            subarray_sum = max(subarray_sum, curr_sum)

        return subarray_sum
```

---

## Complexity

Time Complexity: **O(n)**  
Space Complexity: **O(1)**

---

# 🥈 Solution 2 — Kadane Without max() (Branch Optimization)

## Idea

Instead of calling `max()` each iteration, we explicitly check:

If curr_sum < 0 → start new subarray  
Else → extend current subarray

This removes repeated function calls and makes the logic clearer.

---

## Code

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subarray_sum = curr_sum = nums[0]

        for i in nums[1:]:
            if curr_sum < 0:
                curr_sum = i
            else:
                curr_sum += i

            subarray_sum = max(subarray_sum, curr_sum)

        return subarray_sum
```

---

# 🥇 Solution 3 — Fully Expanded Conditional Logic

## Idea

This version removes all `max()` calls and replaces them with explicit comparisons.

This demonstrates the **full internal logic behind Kadane's algorithm**.

---

## Code

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subarray_sum = curr_sum = nums[0]

        for i in nums[1:]:
            if curr_sum < 0:
                curr_sum = i
            else:
                curr_sum += i

            if subarray_sum > curr_sum:
                subarray_sum = subarray_sum
            else:
                subarray_sum = curr_sum

        return subarray_sum
```

---

# 📈 Dry Run

Example:

nums = [-2,1,-3,4,-1,2,1,-5,4]

| Element | curr_sum | max_sum |
|--------|----------|---------|
| -2 | -2 | -2 |
| 1 | 1 | 1 |
| -3 | -2 | 1 |
| 4 | 4 | 4 |
| -1 | 3 | 4 |
| 2 | 5 | 5 |
| 1 | 6 | 6 |
| -5 | 1 | 6 |
| 4 | 5 | 6 |

Final Answer = **6**

Subarray = **[4,-1,2,1]**

---

# 🧩 Visualization

Array:
-2   1   -3   4   -1   2   1   -5   4

Best Subarray:
[4  -1  2  1] = 6

---

# 🏁 Key Takeaways

✔ This problem is solved using **Kadane's Algorithm**  
✔ Maintain two variables:

- Current Subarray Sum
- Global Maximum Sum

✔ Restart subarray when running sum becomes negative.

---

# 🔗 Related Problems

Once you master this pattern, these problems become easier:

| Problem | Concept |
|------|------|
| Maximum Circular Subarray | Extended Kadane |
| Maximum Product Subarray | Dynamic Programming |
| Best Time to Buy and Sell Stock | Kadane transformation |
| Maximum Submatrix Sum | 2D Kadane |

---

# 🧠 Kadane's Core Formula

curr_sum = max(curr_sum + nums[i], nums[i])  
max_sum = max(max_sum, curr_sum)

This simple idea powers many **medium and hard array problems**.
