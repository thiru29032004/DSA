# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def inorder(Node):
            if Node==None:
                return
            inorder(Node.left)
            ans.append(Node.val)
            inorder(Node.right)
        inorder(root)
        return ans
        
        