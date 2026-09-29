class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[""]
        for i in s:
            if i=="(":
                stack.append("")
            elif i==")":
                temp=stack.pop()
                stack[-1]+=temp[::-1]
            else:
                stack[-1]+=i
        return stack[0]