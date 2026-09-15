class Solution:
    def reverseKGroup(self, head, k):

        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while True:

            # Find the kth node
            kth = group_prev

            for _ in range(k):
                kth = kth.next

                if not kth:
                    return dummy.next

            group_next = kth.next

            # Reverse the group
            prev = group_next
            current = group_prev.next

            while current != group_next:
                temp = current.next
                current.next = prev
                prev = current
                current = temp

            # Connect previous part to reversed group
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp