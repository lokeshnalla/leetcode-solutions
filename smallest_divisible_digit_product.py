class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        while True:
            # Store current number because we need
            # another variable to extract its digits
            temp = n

            # Calculate product of digits
            product = 1

            while temp > 0:
                digit = temp % 10
                product *= digit
                temp //= 10

            # If digit product is divisible by t,
            # this is the smallest valid number
            if product % t == 0:
                return n

            # Otherwise check the next number
            n += 1