# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        counter = 1
        curr = head

        while curr:
            length += 1
            curr = curr.next

        curr = head

        if n == length:
            head = curr.next

        if length == 1:
            return None
        elif length == 2:
            if n == 1:
                curr.next = None
            else:
                head = curr.next
        else:
            while counter < length - n:
                curr = curr.next
                counter += 1
            
            curr.next = curr.next.next

        return head

