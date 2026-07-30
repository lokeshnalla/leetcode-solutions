# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # No need to reverse if only one node
        if not head or left == right:
            return head

        # Dummy node helps when reversing from the head
        dummy = ListNode(0)
        dummy.next = head

        # Move 'prev' to the node before 'left'
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        # 'curr' points to the first node to be reversed
        curr = prev.next

        # Reverse the sublist
        for _ in range(right - left):

            # Node to move
            temp = curr.next

            # Remove temp from its current position
            curr.next = temp.next

            # Insert temp after prev
            temp.next = prev.next
            prev.next = temp

        return dummy.next