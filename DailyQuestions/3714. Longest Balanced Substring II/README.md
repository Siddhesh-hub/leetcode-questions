# 🧩 Longest Balanced Substring II  
> LeetCode Daily Challenge | Prefix Sum | Hashing | Multi-Case Analysis | O(n) Solution

---

## 🚀 Problem Overview

You are given a string `s` consisting only of characters:

```
'a', 'b', 'c'
```

Return the **length of the longest balanced substring**.

A substring is considered **balanced** if:

> All distinct characters in that substring appear the **same number of times**.

---

## 🔎 Visual Understanding

### Example 1

Input:
```
s = "abbac"
```

Output:
```
4
```

Substring `"abba"`:

| Character | Frequency |
|------------|------------|
| a | 2 |
| b | 2 |

✅ All frequencies equal → Balanced  
✅ Length = 4  

---

### Example 2

Input:
```
s = "abcabc"
```

Output:
```
6
```

| Character | Frequency |
|------------|------------|
| a | 2 |
| b | 2 |
| c | 2 |

✅ Balanced  
✅ Length = 6  

---

### Example 3

Input:
```
s = "aabcc"
```

Output:
```
3
```

Balanced substring: `"abc"`  
Each appears once.

---

## 🧠 Core Insight

Since the string contains only **three possible characters**, a balanced substring can only have:

1️⃣ Exactly **one distinct character**  
2️⃣ Exactly **two distinct characters**  
3️⃣ All **three distinct characters**

We solve each case efficiently.

---

# 🛠️ Approach Breakdown

---

## ✅ Case 1 — Single Character

Any continuous run of a single character is automatically balanced.

Example:

```
"aaaa" → length = 4
```

✔ Track longest consecutive run.

Time Complexity: **O(n)**

---

## ✅ Case 2 — Exactly Two Characters

For any pair among:

```
(a, b), (a, c), (b, c)
```

Balanced condition:

```
count(x) == count(y)
```

### 🎯 Key Trick

Use prefix difference:

```
diff = count(x) - count(y)
```

If the same `diff` appears at two indices:

→ substring between them has equal counts.

### 🔁 Important Reset Rule

If the third character appears:
- Reset tracking
- Because substring can’t remain valid for only two characters

---

### 📊 Visual Representation

For pair (a, b):

Index →   0   1   2   3   4  
String →  a   b   a   b   c  
diff   →  1   0   1   0   reset  

Repeated diff = balanced window.

Time Complexity: **O(3n)**

---

## ✅ Case 3 — All Three Characters

Balanced condition:

```
count(a) == count(b) == count(c)
```

Rewrite as:

```
count(a) - count(b) = 0
count(a) - count(c) = 0
```

Instead of tracking full counts,
track difference pair:

```
key = (count(a) - count(b),
       count(a) - count(c))
```

If same key repeats:

→ substring between those indices is balanced.

---

## 📈 Why This Works

If:

```
prefix_state[i] == prefix_state[j]
```

Then:

```
counts between i and j are equal
```

This is the classic **Prefix-Difference Pattern** used in:

- Equal 0s and 1s problems
- Balanced parentheses variants
- Multi-frequency equality problems

---

# 📊 Algorithm Flow

```
Scan string once
   ↓
Track longest single run
   ↓
For each pair (a,b), (a,c), (b,c):
   Use prefix difference + hashmap
   Reset when third char appears
   ↓
Track 3-character balance using pair-difference key
   ↓
Return maximum length
```

---

# 📈 Complexity Analysis

| Metric | Value |
|--------|--------|
| Time Complexity | **O(n)** |
| Space Complexity | **O(n)** |
| Alphabet Size | 3 |
| Max Length | ≤ 10^5 |

---

# 🧠 Pattern Recognition

This problem demonstrates:

- Prefix Sum Technique
- Difference Hashing
- Multi-case decomposition
- Linear time optimization
- Frequency equality transformation

---

# 🎯 Interview Takeaways

✔ When condition involves equality of frequencies:

```
freq(A) == freq(B) == freq(C)
```

Transform into:

```
freq(A) - freq(B)
freq(A) - freq(C)
```

Track difference states.

✔ Small alphabet size simplifies multi-character balance problems.

✔ Break complex problems into structural cases.

---


⭐ If this helped, consider starring the repository.
