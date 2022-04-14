class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        sum = 0
        while l1 != None or l2 != None:
            if l1 != None:
                sum += l1.val * (pow(10, count))
                l1 = l1.next
            if l2 != None:
                sum += l2.val * (pow(10, count))
                l2 = l2.next
            count += 1
        curr = head = ListNode(sum % 10)
        sum = sum // 10
        while sum != 0:
            curr.next = ListNode(sum % 10)
            curr = curr.next
            sum = sum // 10
        return head
