# 🧩 Longest Balanced Substring I  
> LeetCode Daily Challenge | String | Frequency Analysis | Enumeration

---

## 🚀 Problem Overview

Given a string `s` consisting of lowercase English letters, return the **length of the longest balanced substring**.

A substring is **balanced** if:

> All **distinct characters** in that substring appear the **same number of times**.

---

## 🔎 Visual Understanding

### Example 1

s = "abba"


| Character | Frequency |
|-----------|------------|
| a         | 2          |
| b         | 2          |

✅ All frequencies are equal → Balanced  
✅ Length = 4  

---

### Example 2

s = "abcabc"


| Character | Frequency |
|-----------|------------|
| a         | 2          |
| b         | 2          |
| c         | 2          |

✅ Balanced  
✅ Length = 6  

---

### Example 3

s = "aabbc"


| Character | Frequency |
|-----------|------------|
| a         | 2          |
| b         | 2          |
| c         | 1          |

❌ Not balanced (frequencies differ)

---

## 🧠 Core Insight

For a substring to be balanced:

freq(c1) == freq(c2) == ... == freq(ck)


Where:
- `c1...ck` are distinct characters inside the substring
- Only non-zero frequencies matter

Since:
- Alphabet size = 26
- n ≤ 1000

We can afford an **O(n²)** approach with optimized frequency tracking.

---

## 🛠️ Approach Strategy

### Step 1: Fix Left Boundary
Iterate `i` from `0 → n-1`.

### Step 2: Expand Right Boundary
For each `i`, extend `j` from `i → n-1`.

### Step 3: Maintain Frequency Array
Use an array of size 26:

freq[ord(s[j]) - ord('a')]++


### Step 4: Validate Balance
- Extract non-zero frequencies
- If all are equal → update maximum length

---

## 📊 Algorithm Flow Diagram

Start i
↓
Initialize freq[26]
↓
Expand j →
↓
Update frequency
↓
Check:
Are all non-zero frequencies equal?
↓
Yes → Update answer
No → Continue expanding


---

## 💡 Why Not Sliding Window?

Sliding window works when:
- Conditions are monotonic
- Adding elements doesn't invalidate past structure easily

Here:
- Adding one character may break equality
- Distinct count changes dynamically
- No prefix subtraction trick applies

Therefore:
> Controlled enumeration is cleaner and safer.

---

## 📈 Complexity Analysis

| Metric | Value |
|--------|--------|
| Time Complexity | **O(n² × 26)** |
| Space Complexity | **O(1)** |
| n Constraint | ≤ 1000 |
| Alphabet Size | 26 |

### Why O(1) Space?
Frequency array size is constant (26), independent of `n`.

---

## 🎯 Edge Cases Considered

| Input | Output | Reason |
|-------|--------|--------|
| `"aaaa"` | 4 | Single distinct char |
| `"abc"` | 3 | All appear once |
| `"aabbc"` | 4 | `"aabb"` balanced |
| `"z"` | 1 | Single char |

---

## 🏷️ Pattern Recognition

This problem teaches:

- Frequency counting
- Controlled enumeration
- Recognizing when sliding window fails
- Working with fixed alphabet optimizations

---

## 🔥 Interview Takeaway

If alphabet size is small:
> Don’t over-engineer.  
> Enumeration + frequency array is often optimal.

This demonstrates:
- Strong constraint analysis
- Correct pattern recognition
- Clean implementation thinking

---

## 📌 Tags

`String` `Hashing` `Frequency Counting` `Brute Force Optimization` `Daily Challenge`

---

## 👨‍💻 Author Notes

This solution emphasizes:
- Correct constraint reading
- Avoiding premature optimization
- Writing clean, interview-ready logic

---

⭐ If this helped, consider starring the repo.
