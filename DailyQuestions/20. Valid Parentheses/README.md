# 🚀 20. Valid Parentheses

> **Difficulty:** Easy  
> **Pattern:** Stack (LIFO)  
> **Core Concept:** Balanced Brackets Validation  
> **Data Structure Used:** Stack  

---

# 🧩 Problem Statement

Given a string `s` containing only:

```
'(', ')', '{', '}', '[' , ']'
```

Determine whether the string is **valid**.

---

# ✅ Valid String Conditions

An input string is valid if:

1. Open brackets must be closed by the same type.
2. Open brackets must be closed in the correct order.
3. Every closing bracket must have a corresponding opening bracket.

---

# 📌 Constraints

- `1 <= s.length <= 10⁴`
- `s` consists only of `()[]{}`

---

# 🔎 Examples

| Input | Output | Reason |
|--------|--------|--------|
| `"()"` | `true` | Properly matched |
| `"()[]{}"` | `true` | All independent valid pairs |
| `"(]"` | `false` | Type mismatch |
| `"([])"` | `true` | Correct nesting |
| `"([)]"` | `false` | Incorrect order |

---

# 🧠 Core Insight

This is a **classic Stack problem**.

### Why Stack?

Stack follows:

```
Last In → First Out (LIFO)
```

Brackets must close in **reverse order of opening**.

Example:

```
"([])"
```

Push → `(`  
Push → `[`  
See `]` → matches `[` → pop  
See `)` → matches `(` → pop  

Stack becomes empty → valid ✅

---

# ❌ Why Other Structures Fail

- Queue → FIFO (wrong order)
- Set → No ordering
- Counter → Cannot track nesting order

Only Stack naturally models nested structure.

---

# 🛠 Algorithm Explanation

1. Initialize empty stack.
2. Traverse string character by character.
3. If:
   - Stack not empty AND current bracket matches last opened bracket  
     → Pop from stack
   - Otherwise → Push current character
4. After traversal:
   - If stack empty → Valid
   - Else → Invalid

---

# 💻 Implementation

```python
# DS - Stack
# Why - We can use push and pop in O(n) time to check parenthesis matching

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)

        for i in range(n):
            if stack:
                last_element = stack[-1]
                if self.is_parenthesis_combination(last_element, s[i]):
                    stack.pop()
                    continue
            stack.append(s[i])

        return not stack

    def is_parenthesis_combination(self, last_ele, curr_ele):
        if last_ele == "(" and curr_ele == ")" or \
           last_ele == "[" and curr_ele == "]" or \
           last_ele == "{" and curr_ele == "}":
            return True
        return False
```

---

# 🔍 Dry Run Example

Input:

```
s = "([)]"
```

Step-by-step:

| Character | Stack | Action |
|------------|--------|---------|
| `(` | `(` | Push |
| `[` | `( [` | Push |
| `)` | `( [ )` | No match → Push |
| `]` | `( [ ) ]` | No match → Push |

Stack not empty → ❌ Invalid

---

# 📊 Complexity Analysis

| Metric | Complexity |
|--------|------------|
| Time Complexity | **O(n)** |
| Space Complexity | **O(n)** |

### Why?

- Each character pushed at most once
- Each character popped at most once
- Stack size worst case = n

---

# 🧠 Edge Cases

| Case | Result |
|------|--------|
| `"("` | false |
| `")"` | false |
| `"((("` | false |
| `"()()()"` | true |
| `""` | true (empty stack) |

---

# 🎯 Interview Perspective

Interviewers test:

- Understanding of LIFO
- Matching logic correctness
- Edge case handling
- Clean stack implementation
- Time/space reasoning

Common Mistakes:

- Only counting brackets instead of matching order
- Not checking stack emptiness before pop
- Forgetting nested order validation

---

# 🏁 Key Takeaway

Valid Parentheses is:

- A foundational **Stack problem**
- A base pattern for:
  - Expression evaluation
  - HTML/XML parsing
  - Compiler syntax validation
  - Monotonic stack problems

Mastering this builds strong intuition for stack-based design problems.
