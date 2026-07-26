class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        prev = None

        # Count the number of nodes
        while temp:
            count += 1
            temp = temp.next

        # If the head node needs to be removed
        if count == n:
            return head.next

        temp = head

        # Move to the node that should be removed
        while count > n:
            prev = temp
            temp = temp.next
            count -= 1

        # Remove the node
        prev.next = temp.next

        return head