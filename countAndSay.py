class Solution:
    def countAndSay(self, n: int) -> str:

        # First term of the sequence
        result = "1"

        # Generate the next terms
        for i in range(n - 1):

            temp = ""
            count = 1

            # Traverse the current string
            for j in range(1, len(result)):

                # If current character is same as previous
                if result[j] == result[j - 1]:
                    count += 1

                # Character changed
                else:
                    # Append count and previous character
                    temp += str(count)
                    temp += result[j - 1]

                    # Reset count
                    count = 1

            # Add the last group
            temp += str(count)
            temp += result[-1]

            # Update result
            result = temp

        return result