# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isMirror(p: Optional[TreeNode], q):
    if not p and not q:
        return True
    elif not p or not q:
        return False
    else:
        return p.val == q.val and isMirror(p.left, q.right) and isMirror(p.right, q.left)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        else:
            return isMirror(root.left, root.right)
