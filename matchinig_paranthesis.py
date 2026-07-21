class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to store opening brackets
        a = []

        # Traverse each character in the string
        for i in s:

            # If the character is an opening bracket,
            # push it onto the stack
            if i == "(" or i == "{" or i == "[":
                a.append(i)

            # Otherwise, it is a closing bracket
            else:

                # If the stack is empty, there is no matching
                # opening bracket, so the string is invalid
                if not a:
                    return False

                # Remove the top opening bracket from the stack
                top = a.pop()

                # Check if ')' matches '('
                if i == ")" and top != "(":
                    return False

                # Check if '}' matches '{'
                if i == "}" and top != "{":
                    return False

                # Check if ']' matches '['
                if i == "]" and top != "[":
                    return False

        # If the stack is empty, all brackets were matched correctly.
        # Otherwise, there are unmatched opening brackets.
        return len(a) == 0