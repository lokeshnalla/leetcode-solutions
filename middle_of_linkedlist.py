# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        count=0
        while temp:
            count=count+1
            temp=temp.next
        temp1=head
        count=count//2
        while temp1 and count:
            temp1=temp1.next
            count=count-1
        return temp1

        