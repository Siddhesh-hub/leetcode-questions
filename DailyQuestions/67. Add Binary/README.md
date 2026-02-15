# 🚀 67. Add Binary

> **Difficulty:** Easy  
> **Pattern:** Two Pointers + Carry Propagation  
> **Core Concept:** Binary Simulation  
> **Category:** String Manipulation  

---

# 🧩 Problem Statement

Given two binary strings `a` and `b`, return their sum as a binary string.

The solution must simulate binary addition and handle large inputs efficiently.

---

# 🧠 Problem Classification

| Dimension | Type |
|------------|--------|
| Data Structure | String |
| Technique | Two Pointers |
| Paradigm | Simulation |
| Key Idea | Carry Forward Mechanism |

This is a **right-to-left traversal problem** where we simulate manual binary addition.

---

# ✍️ Intuition

Binary addition rules:

```
0 + 0 = 0
1 + 0 = 1
1 + 1 = 10  (write 0, carry 1)
1 + 1 + 1 = 11 (write 1, carry 1)
```

At each step:

```
total = digit_from_a + digit_from_b + carry
result_bit = total % 2
carry = total // 2
```

We process from **least significant bit → most significant bit**.

---

# 🔍 Visual Dry Run

Example:

```
a = "1010"
b = "1011"
```

Binary addition:

```
        carry:   1 0 1
                  1 0 1 0
                + 1 0 1 1
                -----------
                  1 0 1 0 1
```

Step Table:

| a | b | carry_in | total | result_bit | carry_out |
|---|---|----------|--------|------------|------------|
| 0 | 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 0 | 2 | 0 | 1 |
| 0 | 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 0 | 2 | 0 | 1 |
| - | - | 1 | 1 | 1 | 0 |

Final Result → **10101**

---

# 🛠 Algorithm

1. Initialize two pointers at the end of both strings.
2. Maintain a carry variable.
3. Iterate while:
   - either pointer is valid
   - or carry exists
4. Add digits + carry.
5. Store `(total % 2)`.
6. Update carry `(total // 2)`.
7. Reverse the result at the end.

---

# 💻 Implementation (Optimized)

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
                
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            res.append(str(total % 2))
            carry = total // 2
        
        return ''.join(res[::-1])
```

---

# 📊 Complexity Analysis

| Metric | Complexity |
|--------|------------|
| Time Complexity | **O(n)** |
| Space Complexity | **O(n)** |
| n = max(len(a), len(b)) |

We traverse both strings once and build a result of at most length `n + 1`.

---

# 🧠 Why This Solution Is Optimal

- Single linear pass  
- Constant auxiliary variables  
- Handles unequal string lengths  
- Handles final carry correctly  
- Works for very large binary inputs  
- No integer overflow risk  

---

# 🧩 Pattern Takeaway

This is a foundational problem for:

- Big integer arithmetic  
- Linked list number addition  
- Carry propagation patterns  
- Bit manipulation problems  
- Simulation-based interview questions  

---

# 🎯 Interview Perspective

This problem evaluates:

- Clean pointer management  
- Correct carry logic  
- Edge case handling  
- Ability to simulate mathematical operations precisely  

Mastering this ensures strong fundamentals for medium-level number and bit manipulation problems.
