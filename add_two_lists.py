class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        temp = dummy
        carry = 0

        while l1 or l2 or carry:

            # Take value from l1, or 0 if l1 is finished
            val1 = l1.val if l1 else 0

            # Take value from l2, or 0 if l2 is finished
            val2 = l2.val if l2 else 0

            # Add both digits and previous carry
            total = val1 + val2 + carry

            # Current digit
            digit = total % 10

            # Carry for next addition
            carry = total // 10

            # Create new node
            temp.next = ListNode(digit)
            temp = temp.next

            # Move l1
            if l1:
                l1 = l1.next

            # Move l2
            if l2:
                l2 = l2.next

        return dummy.next