class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0

        # ---- Case 1: Single character runs ----
        count = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                count += 1
            else:
                ans = max(ans, count)
                count = 1
        ans = max(ans, count)

        # ---- Case 2: Two-character combinations ----
        from itertools import combinations

        for c1, c2 in combinations('abc', 2):
            diff_map = {0: -1}
            diff = 0
            for i, ch in enumerate(s):
                if ch == c1:
                    diff += 1
                elif ch == c2:
                    diff -= 1
                else:
                    diff = 0
                    diff_map = {0: i}
                    continue

                if diff in diff_map:
                    ans = max(ans, i - diff_map[diff])
                else:
                    diff_map[diff] = i

        # ---- Case 3: All three characters ----
        count_a = count_b = count_c = 0
        diff_map = {(0, 0): -1}

        for i, ch in enumerate(s):
            if ch == 'a':
                count_a += 1
            elif ch == 'b':
                count_b += 1
            else:
                count_c += 1

            key = (count_a - count_b, count_a - count_c)

            if key in diff_map:
                ans = max(ans, i - diff_map[key])
            else:
                diff_map[key] = i

        return ans
