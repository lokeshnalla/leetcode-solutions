class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(s):
            count = 0

            for ch in s:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                if count < 0:
                    return False

            return count == 0

        level = {s}

        while level:
            valid = [x for x in level if isValid(x)]

            if valid:
                return valid

            next_level = set()

            for x in level:
                for i, ch in enumerate(x):
                    if ch not in "()":
                        continue

                    next_level.add(x[:i] + x[i + 1:])

            level = next_level

        return [""]