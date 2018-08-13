# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        #this strategy just iterates recursively through each list
        #there are definitely more efficient ways to write code
        
        #another way here (iterative): https://leetcode.com/problems/add-two-numbers/discuss/1016/Clear-python-code-straight-forward
        if (l1 == None):
            return l2
        if (l2 == None):
            return l1
        
        val = (l1.val + l2.val) % 10
        rem = (l1.val + l2.val) // 10
        
        sum = ListNode(val)
        sum.next = self.addTwoNumbersUtil(l1.next, l2.next, rem)
        return sum
    
    def addTwoNumbersUtil(self, l1, l2, rem):
        if (rem <= 0):
            if (l1 == None):
                return l2
            elif (l2 == None):
                return l1
        elif (rem > 0 and l1 == None and l2 == None):
            sum = ListNode(rem)
            return sum
        elif (rem > 0 and l1 == None):
            l1 = ListNode(0)
            l1.next = None
        elif (rem > 0 and l2 == None):
            l2 = ListNode(0)
            l2.next = None
        
        
        val = (l1.val + l2.val + rem) % 10
        rem = (l1.val + l2.val + rem) // 10
        sum = ListNode(val)
        sum.next = self.addTwoNumbersUtil(l1.next, l2.next, rem)
        return sum
        
        
        
        
