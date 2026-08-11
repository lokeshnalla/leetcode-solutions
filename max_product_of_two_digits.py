class Solution:
    def maxProduct(self, n: int) -> int:

        # Store the largest and second largest digits
        max1 = 0
        max2 = 0

        # Process each digit of n
        while n > 0:

            # Get the last digit
            a = n % 10

            # If current digit is greater than max1
            if a > max1:

                # Old max1 becomes second largest
                max2 = max1

                # Current digit becomes largest
                max1 = a

            # If current digit is between max1 and max2
            elif a > max2:
                max2 = a

            # Remove the last digit
            n = n // 10

        # Return product of two largest digits
        return max1 * max2