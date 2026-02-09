🌳 Balance a Binary Search Tree (LeetCode)
📌 Problem Statement

Given the root of a Binary Search Tree (BST), return a balanced BST with the same node values.

A balanced BST is defined as a tree where for every node, the height difference between its left and right subtrees is at most 1.

Example

Input (Unbalanced BST):

    1
     \
      2
       \
        3
         \
          4


Output (Balanced BST):

      2
     / \
    1   3
         \
          4


The structure may vary, but the BST must be height-balanced.

🧠 Key Observations

Inorder traversal of a BST produces a sorted sequence.

A balanced BST can be constructed from a sorted array by:

Choosing the middle element as root

Recursively building left and right subtrees

The problem reduces to:

Convert BST → sorted array

Convert sorted array → balanced BST

🛠️ Approach
Step 1: Inorder Traversal

Traverse the BST in inorder fashion and store node values in a list.

Left → Root → Right


This guarantees sorted order because of BST properties.

Step 2: Build Balanced BST

Use a divide-and-conquer approach:

Pick middle element as root

Recursively build left subtree from left half

Recursively build right subtree from right half

This ensures the height difference is minimized.

✅ Algorithm

Perform inorder traversal and store values in an array.

Recursively build a balanced BST using the sorted array.

Return the new root.

⏱️ Complexity Analysis
Metric	Complexity
Time Complexity	O(N)
Space Complexity	O(N) (inorder array + recursion stack)

Where N is the number of nodes in the BST.

🧠 Important Notes (Interview Perspective)

This solution does not rebalance in-place; it rebuilds the tree.

Inorder traversal is the key insight — without it, this problem is difficult.

This pattern is reusable for:

Convert sorted array to BST

Rebalancing skewed trees

Tree reconstruction problems

Recursion depth can reach O(N) in worst-case skewed trees.

🔁 Related Problems

Convert Sorted Array to Binary Search Tree

Validate Binary Search Tree

Balanced Binary Tree

Binary Tree Inorder Traversal

🎯 Takeaway

BST + inorder traversal = sorted data
Sorted data + mid selection = balanced BST

Understanding this transformation is more important than memorizing the code.
