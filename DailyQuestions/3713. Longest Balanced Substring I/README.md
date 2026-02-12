🧩 Longest Balanced Substring I
📌 Problem Statement

Given a string s consisting of lowercase English letters, return the length of the longest balanced substring.

A substring is considered balanced if:

All distinct characters in the substring appear the same number of times.

🧠 Understanding the Problem

For any substring:

Let freq[c] be the frequency of character c

Let the set of distinct characters be {c1, c2, ..., ck}

The substring is balanced if:

freq[c1] == freq[c2] == ... == freq[ck]

🔎 Examples
Input	Output	Explanation
"abba"	4	'a' appears 2 times, 'b' appears 2 times
"abc"	3	Each character appears once
"aaaa"	4	Only one distinct character, frequency = 4
🔍 Key Observations

We must evaluate substrings (contiguous).

The condition applies only to distinct characters inside that substring.

The alphabet size is fixed (26 lowercase letters).

Since substring count is O(n²), we need an efficient way to check balance.

🚀 Approach
Brute Force Strategy (Optimized)

Fix a starting index i.

Expand the ending index j.

Maintain:

A frequency array of size 26.

Count of distinct characters.

At every step:

Collect non-zero frequencies.

If all non-zero frequencies are equal → substring is balanced.

Update maximum length.

Because the alphabet size is constant (26), checking frequencies is efficient.

📊 Complexity Analysis

Time Complexity:
O(n² × 26)
(Two nested loops + constant alphabet check)

Space Complexity:
O(1)
(Fixed 26-length frequency array)

This works well for constraints where n ≤ 1000.

📝 Why Not Use Sliding Window?

A typical sliding window approach does not work directly because:

Frequency equality must hold across all distinct characters.

Adding a character can disturb balance in non-monotonic ways.

Distinct character count dynamically changes.

Hence, controlled enumeration is safer and simpler.

🎯 Important Notes

A substring with only one distinct character is considered balanced.

Always check only non-zero frequencies.

Avoid recalculating frequency maps from scratch inside inner loops.

🧠 Key Takeaways

Problems involving equal frequency of all distinct characters are not prefix-friendly.

When alphabet size is small, brute force with frequency tracking is acceptable.

Always analyze constraints before over-optimizing.

Recognize when sliding window is inappropriate.

📌 Pattern Category

String

Frequency Counting

Enumeration

Hashing
