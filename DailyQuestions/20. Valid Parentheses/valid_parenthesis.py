# DS - Stack
# Why - We can use push and pop in time O(n) time to check parenthesis and combination
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
        if last_ele == "(" and curr_ele==")" or last_ele == "[" and curr_ele=="]" or last_ele == "{" and curr_ele=="}":
            return True
        return False
