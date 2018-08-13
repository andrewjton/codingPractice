# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #recursive
    def inorderTraversalRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if (root == None):
            return []
        l = list()
        l = l + (self.inorderTraversal(root.left))
        l.append(root.val)
        l = l + (self.inorderTraversal(root.right))
        return l
    
    #iterative
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        stack = list()
        curr = root
        res = list()
        
        while (stack or curr):
            while(curr): #push all left elements
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
            
        return res