class Solution:
    def checkDivisibility(self, n: int) -> bool:

        # Save the original number
        original = n

        # Sum of digits
        s = 0

        # Product of digits
        p = 1

        # Extract each digit
        while n > 0:
            a = n % 10

            # Add digit to sum
            s += a

            # Multiply digit into product
            p *= a

            # Remove last digit
            n //= 10

        # Sum + product of digits
        fs = s + p

        # Check original number
        if original % fs == 0:
            return True
        else:
            return False