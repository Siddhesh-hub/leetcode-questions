# 🚀 1. Two Sum

> **Difficulty:** Easy  
> **Pattern:** HashMap + Complement Technique  
> **Core Concept:** Instant Lookup Optimization  
> **Category:** Array / Hashing  

---

# 🧩 Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

### Constraints:
- Exactly one solution exists.
- You may not use the same element twice.
- You can return the answer in any order.

---

# 🧠 Problem Understanding

We must:

- Find two **different indices**
- Such that:
  
  ```
  nums[i] + nums[j] = target
  ```

Since exactly one solution is guaranteed, we can stop once found.

---

# 🔴 Brute Force Approach (Baseline Thinking)

Check every possible pair.

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
```

### Complexity

| Metric | Complexity |
|--------|------------|
| Time | O(n²) |
| Space | O(1) |

Too slow for large inputs.

---

# 🟢 Optimized Approach — HashMap (Complement Pattern)

## 💡 Core Idea

For every number:

```
needed = target - current_number
```

If `needed` was seen before, we found our pair.

Instead of scanning the array again, we store previously seen numbers in a HashMap.

This reduces lookup time from O(n) → O(1).

---

# 🔍 Dry Run

Example:

```
nums = [2, 7, 11, 15]
target = 9
```

### Step 1:
```
num = 2
needed = 7
hashmap = {}
```
Not found → store `{2: 0}`

### Step 2:
```
num = 7
needed = 2
```
2 exists in hashmap → return `[0, 1]`

---

# 💻 Final Implementation

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            needed = target - num
            
            if needed in hashmap:
                return [hashmap[needed], i]
            
            hashmap[num] = i
```

---

# 📊 Complexity Analysis

| Metric | Complexity |
|--------|------------|
| Time Complexity | **O(n)** |
| Space Complexity | **O(n)** |

- Each element processed once.
- HashMap lookup is O(1).
- Worst-case space stores all elements.

---

# 🧠 Why HashMap Works

Instead of checking all pairs:

```
For each element → search entire array
```

We switch to:

```
Store elements seen so far → check complement instantly
```

HashMap allows constant-time complement lookup.

---

# 🔎 Pattern Recognition

This problem introduces the **Complement Pattern**:

```
target - current_value
```

Whenever you see:

- Pair sum problems  
- Frequency matching  
- Subarray sum variants  
- Complement-based matching  

→ Think **HashMap**.

---

# 🎯 Interview Perspective

Interviewers expect:

- Brute force first
- Then optimization discussion
- Recognition of complement logic
- Proper handling of index reuse constraint
- Clean implementation

Two Sum is foundational for:

- 3Sum
- 4Sum
- Subarray Sum Equals K
- Pair difference problems
- Sliding window + hashing combinations

---

# 🏁 Key Takeaway

Two Sum teaches a core DSA mindset shift:

From:

```
Search repeatedly
```

To:

```
Store and lookup instantly
```

Mastering this pattern unlocks a wide class of hashing problems.
