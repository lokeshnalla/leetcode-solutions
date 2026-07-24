class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Set to store visited nodes
        visited = set()

        # Traverse the linked list
        while head:

            # If node is already visited, cycle exists
            if head in visited:
                return True

            # Store current node
            visited.add(head)

            # Move to the next node
            head = head.next

        # Reached end of list, so no cycle
        return False