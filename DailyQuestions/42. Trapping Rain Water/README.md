# 🚀 42. Trapping Rain Water

> **Difficulty:** Hard  
> **Pattern:** Two Pointers + Prefix Maximums  
> **Category:** Array / Dynamic Programming Optimization  
> **Core Idea:** Water Level Determined by Minimum of Left Max and Right Max

---

# 🧩 Problem Statement

Given `n` non-negative integers representing an elevation map where the width of each bar is **1**, compute how much **rainwater can be trapped** after raining.

The array represents bar heights.

```
height[i] = elevation at index i
```

Water can only be trapped **between taller bars**.

---

# 📌 Constraints

| Constraint | Value |
|-------------|------|
| Number of bars | `1 <= n <= 2 * 10^4` |
| Height range | `0 <= height[i] <= 10^5` |

---

# 🔎 Examples

### Example 1

```
Input:
height = [0,1,0,2,1,0,1,3,2,1,2,1]

Output:
6
```

Visualization:

```
      █
  █   ██
█ ██ ████
------------
```

Blue water trapped = **6 units**

---

### Example 2

```
Input:
height = [4,2,0,3,2,5]

Output:
9
```

---

# 🧠 Key Insight

Water trapped at any index depends on **the tallest bar on both sides**.

```
water[i] = min(max_left, max_right) - height[i]
```

Where:

```
max_left  = highest bar to the left
max_right = highest bar to the right
```

---

# 🔍 Visual Explanation

Example:

```
height = [4,2,0,3,2,5]
```

| Index | Height | Max Left | Max Right | Water |
|------|-------|----------|-----------|------|
|0|4|4|5|0|
|1|2|4|5|2|
|2|0|4|5|4|
|3|3|4|5|1|
|4|2|4|5|2|
|5|5|5|5|0|

Total Water:

```
2 + 4 + 1 + 2 = 9
```

---

# ❌ Brute Force Approach

For each index:

1. Find maximum left height
2. Find maximum right height
3. Compute trapped water

### Complexity

| Metric | Complexity |
|------|-------------|
| Time | **O(n²)** |
| Space | **O(1)** |

Too slow for large inputs.

---

# 🟢 Optimized Two-Pointer Approach

Instead of computing left/right max repeatedly, we track them dynamically.

We maintain:

```
left pointer
right pointer
left_max
right_max
```

### Key Idea

If:

```
height[left] < height[right]
```

Then the water level depends on **left_max**.

Otherwise it depends on **right_max**.

This allows computing water in **one pass**.

---

# 📊 Algorithm Steps

1️⃣ Initialize:

```
left = 0
right = n-1
left_max = 0
right_max = 0
water = 0
```

2️⃣ Move pointers inward.

3️⃣ Update maximum heights.

4️⃣ Calculate trapped water.

5️⃣ Continue until pointers meet.

---

# 💻 Implementation

```python
class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        
        left_max = 0
        right_max = 0
        
        water = 0
        
        while left < right:

            if height[left] < height[right]:

                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]

                left += 1

            else:

                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]

                right -= 1
        
        return water
```

---

# 📈 Complexity Analysis

| Metric | Complexity |
|------|-------------|
| Time Complexity | **O(n)** |
| Space Complexity | **O(1)** |

### Why O(n)?

Each pointer moves across the array **only once**.

---

# 🧠 Why the Two Pointer Trick Works

The water level depends on the **smaller boundary**.

```
min(left_max, right_max)
```

If:

```
height[left] < height[right]
```

Then:

```
left side determines water level
```

Because the right boundary is guaranteed to be higher.

---

# 🔥 Common Mistakes

❌ Trying brute force for each index  
❌ Forgetting that water depends on **minimum boundary**  
❌ Updating water before updating `left_max` / `right_max`  
❌ Using extra arrays unnecessarily  

---

# 🎯 Interview Pattern

This problem is a **classic two-pointer optimization** and appears frequently in interviews.

Related problems:

- Container With Most Water
- Largest Rectangle in Histogram
- Trapping Rain Water II
- Maximum Area Problems

---

# 🏁 Key Takeaway

The most important realization is:

```
Water level = min(left_max, right_max)
```

Using two pointers allows us to compute trapped water **in a single linear scan**, reducing the complexity from:

```
O(n²) → O(n)
```

with **constant extra space**.
