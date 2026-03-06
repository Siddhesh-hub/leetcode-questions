# 🚀 121. Best Time to Buy and Sell Stock

> **Difficulty:** Easy  
> **Pattern:** Kadane's Algorithm / Greedy / Single Pass Optimization  
> **Data Structure:** Array  
> **Category:** Dynamic Programming Pattern (Maximum Subarray Variant)

---

# 🧩 Problem Statement

You are given an array `prices` where:

```
prices[i] = stock price on day i
```

You must choose:

1️⃣ One day to **buy** a stock  
2️⃣ A later day to **sell** that stock  

Your goal is to **maximize profit**.

```
profit = sell_price - buy_price
```

### Important Constraints

- You **must buy before selling**
- Only **one transaction** is allowed
- If no profit is possible → return **0**

---

# 📌 Constraints

| Constraint | Value |
|-------------|------|
| Number of days | `1 <= prices.length <= 10^5` |
| Price range | `0 <= prices[i] <= 10^4` |

---

# 🔎 Examples

### Example 1

```
Input:
prices = [7,1,5,3,6,4]

Output:
5
```

Explanation:

```
Buy  at price = 1
Sell at price = 6

Profit = 6 - 1 = 5
```

---

### Example 2

```
Input:
prices = [7,6,4,3,1]

Output:
0
```

Explanation:

Prices continuously decrease → **no profitable transaction possible**

---

# 🧠 Key Observation

Profit is calculated as:

```
profit = selling_price - buying_price
```

To maximize profit:

✔ Buy at the **lowest price seen so far**  
✔ Sell at the **highest price after buying**

Instead of checking all pairs (`O(n²)`), we can track:

```
minimum price so far
maximum profit so far
```

This leads to a **single pass greedy solution**.

---

# 💡 Algorithm Idea (Kadane Inspired)

This solution is conceptually similar to **Kadane's Algorithm** (Maximum Subarray Sum).

Instead of summing values, we track the **maximum difference** between prices.

### Strategy

At every day:

1️⃣ Update the **minimum buying price**

```
buy = min(buy, current_price)
```

2️⃣ Calculate potential profit

```
current_profit = current_price - buy
```

3️⃣ Update maximum profit

```
profit = max(profit, current_profit)
```

---

# 📊 Visual Explanation

Example:

```
prices = [7,1,5,3,6,4]
```

| Day | Price | Minimum Buy | Potential Profit | Max Profit |
|----|------|-------------|-----------------|------------|
|1|7|7|0|0|
|2|1|1|0|0|
|3|5|1|4|4|
|4|3|1|2|4|
|5|6|1|5|5|
|6|4|1|3|5|

Final Answer:

```
5
```

---

# 💻 Implementation

```python
class Solution:
    # Using Kadane's Algorithm style greedy approach
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        n = len(prices)

        for i in range(1, n):

            if prices[i] < buy:
                buy = prices[i]

            elif prices[i] - buy > profit:
                profit = prices[i] - buy

        return profit
```

---

# 📈 Complexity Analysis

| Metric | Complexity |
|------|-------------|
| Time Complexity | **O(n)** |
| Space Complexity | **O(1)** |

### Why O(n)?

We scan the array **only once**.

### Why O(1) Space?

We only maintain two variables:

```
buy
profit
```

No additional data structures are used.

---

# ⚠️ Edge Cases

| Scenario | Result |
|--------|-------|
| Prices always decreasing | 0 |
| Only one day price | 0 |
| Same price every day | 0 |
| Minimum price appears late | handled correctly |

Example:

```
[7,6,4,3,1]
```

Output:

```
0
```

---

# 🔥 Pattern Recognition

This problem teaches an important interview pattern:

```
Track Minimum Value So Far
```

Used in problems like:

- Best Time to Buy and Sell Stock II
- Maximum Difference in Array
- Maximum Subarray (Kadane)
- Stock Trading DP problems

---

# 🎯 Key Takeaways

✔ Only **one pass** is required  
✔ Maintain **minimum price so far**  
✔ Continuously compute **maximum profit**  
✔ Classic **Greedy + Kadane style optimization**

---

# 🏁 Final Insight

The key trick is realizing:

```
Max Profit = Maximum Difference Between Two Elements
```

Where:

```
smaller element appears before larger element
```

This transforms an **O(n²)** brute force problem into an **O(n)** optimal solution.
