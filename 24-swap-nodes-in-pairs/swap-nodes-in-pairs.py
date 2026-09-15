class Solution:
    def swapPairs(self, head):

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while prev.next and prev.next.next:

            first = prev.next
            second = first.next

            # Swap the two nodes
            first.next = second.next
            second.next = first
            prev.next = second

            # Move to the next pair
            prev = first

        return dummy.next