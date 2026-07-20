class Solution:
    def myAtoi(self, s: str) -> int:

        # Remove leading and trailing spaces
        s = s.strip()

        # If string becomes empty
        if not s:
            return 0

        i = 0
        j = len(s) - 1

        sign = 1

        # Check sign
        if s[i] == "-":
            sign = -1
            i += 1

        elif s[i] == "+":
            i += 1

        num = 0

        # Read digits
        while i <= j and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        # Apply sign
        num *= sign

        # Handle overflow
        if num > 2**31 - 1:
            return 2**31 - 1

        if num < -2**31:
            return -2**31

        return num