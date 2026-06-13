# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = l1
        firstDigits = []
        secondDigits = []

        while curr:
            firstDigits.append(curr.val)
            curr = curr.next

        curr = l2

        while curr:
            secondDigits.append(curr.val)
            curr = curr.next

        firstDigits.reverse()
        secondDigits.reverse()

        firstNumber = int("".join(map(str, firstDigits)))
        secondNumber = int("".join(map(str, secondDigits)))

        total = firstNumber + secondNumber

        res = [int(digit) for digit in str(total)]
        res.reverse()

        dummy = ListNode()
        curr = dummy

        for d in res:
            curr.next = ListNode(d)
            curr = curr.next

        return dummy.next


