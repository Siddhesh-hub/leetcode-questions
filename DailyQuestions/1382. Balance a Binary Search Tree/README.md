# 🌳 Balance a Binary Search Tree (LeetCode)

## 📌 Problem Statement
Given the `root` of a **Binary Search Tree (BST)**, return a **height-balanced BST** containing the same node values.

A BST is considered **balanced** if, for every node, the height difference between its left and right subtrees is **at most 1**.

The returned tree must satisfy both:
- Binary Search Tree property
- Height-balanced property

---

## 🧠 Key Observations
1. Inorder traversal of a BST always produces values in **sorted order**.
2. A balanced BST can be constructed from a sorted sequence by choosing the **middle element** as the root.
3. Rebuilding the tree using divide-and-conquer guarantees minimal height.
4. The exact structure of the balanced BST may differ, but correctness depends on balance and BST validity.

---

## 🛠️ Approach
1. Traverse the BST using **inorder traversal** and store all node values.
2. Use the sorted values to reconstruct a balanced BST:
   - Select the middle value as root
   - Recursively build left subtree from left half
   - Recursively build right subtree from right half
3. Return the newly constructed balanced BST.

This approach ensures the height difference between left and right subtrees remains minimal.

---

## ⏱️ Complexity Analysis
| Metric | Complexity |
|------|-----------|
| Time Complexity | O(N) |
| Space Complexity | O(N) |

Where **N** is the total number of nodes in the BST.

---

## 🧠 Important Notes
- The tree is **rebuilt**, not balanced in-place.
- Inorder traversal is the key insight that simplifies the problem.
- The algorithm works for both skewed and already balanced BSTs.
- Recursion depth may reach O(N) in worst-case skewed trees.
- This technique is widely applicable to tree reconstruction problems.

---

## 🎯 Key Takeaway
**BST + inorder traversal → sorted sequence**  
**Sorted sequence + midpoint selection → balanced BST**

Understanding this transformation is crucial for solving many BST-related interview problems.
