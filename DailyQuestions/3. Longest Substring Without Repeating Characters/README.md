# 🚀 3. Longest Substring Without Repeating Characters

> **Difficulty:** Medium  
> **Pattern:** Sliding Window + HashSet  
> **Core Concept:** Dynamic Window Expansion & Shrinking  
> **Category:** String / Two Pointers  

---

# 🧩 Problem Statement

Given a string `s`, return the length of the **longest substring** without repeating characters.

⚠ Important:
- A substring is **contiguous**.
- A subsequence is NOT valid for this problem.

---

# 📌 Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

---

# 🔎 Examples

### Example 1
```
Input:  "abcabcbb"
Output: 3
Explanation: "abc"
```

---

### Example 2
```
Input:  "bbbbb"
Output: 1
Explanation: "b"
```

---

### Example 3
```
Input:  "pwwkew"
Output: 3
Explanation: "wke"
```

⚠ "pwke" is not valid because it is a subsequence, not a substring.

---

# 🧠 Core Insight

Brute force would try all substrings → O(n³).

Instead, we use:

# 🟢 Sliding Window Technique

We maintain a window:

```
[left -------- right]
```

Rules:

- Expand `right`
- If duplicate found → shrink from `left`
- Maintain a set for O(1) lookup

---

# ❌ Why Brute Force Fails

Brute force:

```
for i:
    for j:
        check substring uniqueness
```

### Complexity:

| Metric | Complexity |
|--------|------------|
| Time | O(n³) |
| Space | O(n) |

For `n = 50,000` → Impossible ❌

---

# 🟢 Optimized Sliding Window Approach

### Idea:

1. Use a set to track characters in current window.
2. Expand right pointer.
3. If duplicate found:
   - Remove left character
   - Move left pointer
   - Repeat until duplicate removed.
4. Track max length.

---

# 💻 Implementation

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        left = 0
        char_set = set()

        for right in range(n):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
```

---

# 🔍 Dry Run

Example:

```
s = "abcabcbb"
```

| Step | Left | Right | Window | Max |
|------|------|-------|--------|-----|
| a | 0 | 0 | a | 1 |
| b | 0 | 1 | ab | 2 |
| c | 0 | 2 | abc | 3 |
| a | shrink | 3 | bca | 3 |
| b | shrink | 4 | cab | 3 |

Final answer = **3**

---

# 📊 Complexity Analysis

| Metric | Complexity |
|--------|------------|
| Time Complexity | **O(n)** |
| Space Complexity | **O(n)** |

### Why O(n)?

Each character:
- Added once
- Removed once

Total operations ≤ 2n.

---

# 🧠 Key Observations

- We never restart scanning.
- We dynamically adjust the window.
- Duplicate handling is incremental, not reset-based.

---

# 🔥 Common Mistakes

❌ Restarting window completely  
❌ Not removing characters when duplicate found  
❌ Using string concatenation (O(n))  
❌ Confusing substring with subsequence  
❌ Using brute-force nested loops  

---

# 🎯 Interview Perspective

Interviewers evaluate:

- Recognition of sliding window pattern
- Efficient duplicate handling
- Correct pointer movement
- Time complexity reasoning

This problem is foundational for:

- Minimum Window Substring
- Longest Repeating Character Replacement
- Permutation in String
- Subarray with K Distinct Characters

---

# 🏁 Key Takeaway

This problem teaches:

- Sliding window mastery
- Two pointer control
- Efficient duplicate detection
- Transforming O(n²) → O(n)

Mastering this pattern unlocks many advanced string and array problems.
