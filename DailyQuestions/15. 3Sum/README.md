# 🚀 15. 3Sum

> **Difficulty:** Medium  
> **Pattern:** Sorting + Two Pointers  
> **Core Concept:** Complement Reduction (3Sum → 2Sum)  
> **Category:** Array / Two Pointer Technique  

---

# 🧩 Problem Statement

Given an integer array `nums`, return all the triplets:

```
[nums[i], nums[j], nums[k]]
```

Such that:

- `i != j`
- `i != k`
- `j != k`
- `nums[i] + nums[j] + nums[k] == 0`

### Important:
- The solution set must NOT contain duplicate triplets.
- Order of output does not matter.

---

# 📌 Constraints

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

---

# 🧠 Problem Understanding

We must:

1. Pick three different indices
2. Their values must sum to `0`
3. No duplicate triplets allowed

---

# 🔴 Brute Force Approach (Why Not?)

Try all triplets:

```
for i:
    for j:
        for k:
```

### Complexity

| Metric | Complexity |
|--------|------------|
| Time | O(n³) |
| Space | O(1) |

For `n = 3000`:

```
3000³ = 27,000,000,000 ❌
```

Too slow.

---

# 🟢 Optimized Approach — Sorting + Two Pointers

## 💡 Core Insight

We reduce 3Sum to 2Sum.

For each fixed number:

```
nums[i] + nums[l] + nums[r] = 0
```

Rearrange:

```
nums[l] + nums[r] = -nums[i]
```

So:

👉 Fix one number  
👉 Solve Two Sum on the remaining array  

---

# 🔍 Why Sorting Is Required

Sorting allows:

- Two-pointer traversal
- Duplicate skipping
- Ordered movement of pointers

Without sorting → duplicate handling becomes complex.

---

# 🛠 Algorithm Steps

1. Sort the array.
2. Fix one element at index `i`.
3. Use two pointers:
   - `l = i + 1`
   - `r = n - 1`
4. If sum is:
   - Equal → store result
   - Less → move left pointer
   - Greater → move right pointer
5. Skip duplicates at:
   - Fixed element
   - Left pointer
   - Right pointer

---

# 🔎 Visual Example

Input:

```
nums = [-1,0,1,2,-1,-4]
```

After sorting:

```
[-4, -1, -1, 0, 1, 2]
```

Triplets found:

```
[-1, -1, 2]
[-1, 0, 1]
```

---

# 💻 Final Implementation

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        final_result = []

        # Fix the first element
        for i in range(0, n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = n - 1

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

                    # Skip duplicates for r
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                elif nums[l] + nums[r] < needed:
                    l += 1
                else:
                    r -= 1

        return final_result
```

---

# 📊 Complexity Analysis

| Metric | Complexity |
|--------|------------|
| Time Complexity | **O(n²)** |
| Space Complexity | **O(1)** (excluding output) |

### Explanation

- Sorting → O(n log n)
- Outer loop → O(n)
- Inner two-pointer → O(n)
- Total → O(n²)

---

# 🧠 Why Duplicate Skipping Is Critical

Without skipping duplicates:

```
[0,0,0,0]
```

Would produce:

```
[[0,0,0], [0,0,0]]
```

But expected:

```
[[0,0,0]]
```

So we must skip duplicates at:

- Fixed index `i`
- Left pointer `l`
- Right pointer `r`

---

# 🔎 Pattern Recognition

3Sum is an extension of:

- Two Sum
- Complement Pattern

General Flow:

```
Fix one element → Solve 2Sum on remaining
```

This pattern extends to:

- 4Sum
- kSum problems
- Target-based combinations

---

# 🎯 Interview Perspective

Interviewers evaluate:

- Recognition of sorting necessity
- Two-pointer control
- Duplicate handling logic
- Time complexity reasoning
- Clean pointer movement

Common mistakes:

- Not skipping duplicates
- Infinite loops
- Wrong pointer updates

---

# 🏁 Key Takeaway

3Sum teaches:

- Problem reduction (3Sum → 2Sum)
- Two-pointer mastery
- Duplicate control strategy
- Pattern-based thinking

Mastering 3Sum builds strong foundations for advanced k-Sum and combination problems.
