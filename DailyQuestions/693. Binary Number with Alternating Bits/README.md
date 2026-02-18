# 🚀 693. Binary Number with Alternating Bits

> **Difficulty:** Easy  
> **Pattern:** Bit Manipulation  
> **Core Concept:** Adjacent Bit Validation  
> **Category:** Binary Representation / XOR Trick  

---

# 🧩 Problem Statement

Given a positive integer `n`, return `true` if its binary representation has alternating bits.

An integer has alternating bits if no two adjacent bits are equal.

---

## 🔹 Example 1

```
Input:  n = 5
Output: true
Explanation: 5 → 101 (alternating)
```

## 🔹 Example 2

```
Input:  n = 7
Output: false
Explanation: 7 → 111 (not alternating)
```

---

# 🧠 Approach 1 — Binary String Traversal

## 💡 Idea

1. Convert `n` to binary.
2. Traverse the binary string.
3. Check if any adjacent bits are equal.
4. If equal → return `False`.
5. Otherwise → return `True`.

---

## 🔍 Visual

```
n = 10
Binary = 1010
```

Check pairs:

| Previous | Current | Valid? |
|----------|----------|---------|
| 1 | 0 | ✅ |
| 0 | 1 | ✅ |
| 1 | 0 | ✅ |

All valid → ✅ True

---

## 💻 Implementation

```python
class Solution: 
    def hasAlternatingBits(self, n: int) -> bool:
        bin_n = bin(n)[2:]
        len_n = len(bin_n)
        for i in range(1, len_n):
            if bin_n[i] == bin_n[i - 1]:
                return False
        return True
```

---

## 📊 Complexity Analysis (Approach 1)

| Metric | Complexity |
|--------|------------|
| Time Complexity | **O(log n)** |
| Space Complexity | **O(log n)** |

Binary conversion takes `log₂(n)` bits.

---

# 🚀 Approach 2 — Optimized Bitwise XOR Trick (Interview-Level)

## 💡 Core Insight

If a number has alternating bits:

```
n = 101010...
```

Then:

```
n >> 1 = 010101...
```

Now:

```
n ^ (n >> 1) = 111111...
```

If the result is all 1s, then the original number had alternating bits.

Now the question becomes:

👉 How do we check if a number is all 1s?

A number is all 1s if:

```
x & (x + 1) == 0
```

Because:

```
1111 & 10000 = 0000
```

---

## 🔍 Visual Example

```
n = 5
Binary = 101

n >> 1 = 010

XOR:
101
010
---
111   (all 1s)
```

Now check:

```
111 & 1000 = 0
```

Condition satisfied → Alternating → ✅ True

---

## 💻 Implementation (Optimized)

```python
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        xor_n = (n ^ (n >> 1))
        return True if (xor_n & (xor_n + 1)) == 0 else False
```

---

## 📊 Complexity Analysis (Approach 2)

| Metric | Complexity |
|--------|------------|
| Time Complexity | **O(1)** |
| Space Complexity | **O(1)** |

All operations are constant-time bitwise operations.

---

# 🧠 Why XOR Trick Works

For alternating bits:

```
n        = 101010
n >> 1   = 010101
XOR      = 111111
```

Only alternating sequences produce a continuous sequence of 1s after XOR.

Checking `(x & (x + 1)) == 0` verifies that the number is of the form:

```
111...111
```

---

# 🔎 Comparison of Approaches

| Approach | Time | Space | Interview Impact |
|----------|------|--------|------------------|
| String Traversal | O(log n) | O(log n) | Basic |
| XOR Trick | O(1) | O(1) | ⭐ High |

---



# 🏁 Final Takeaway

This problem teaches:

- Binary representation reasoning  
- Bit shifting  
- XOR behavior  
- Detecting special bit patterns  

Mastering such patterns builds strong foundations for advanced bit manipulation problems.
