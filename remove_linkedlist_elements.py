class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        temp = head

        while temp:

            if temp.val == val:
                prev.next = temp.next
            else:
                prev = temp

            temp = temp.next

        return dummy.next