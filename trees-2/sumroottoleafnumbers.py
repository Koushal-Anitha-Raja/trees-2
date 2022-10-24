#TC:O(n)
#SC:0(H)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        #appending all the curr sum values in result variable
        self.result=0
        #returning the inorder tarversal function
        self.inordertraversal(root,0)
        return self.result
        
        #inorder function 
        #currsum is changing so we are giving it as a parameter
    def inordertraversal(self,root,currsum):
        #base condition
        if root==None:
            return
        #logic
        
        currsum=currsum*10+root.val
        print(currsum)
        #checking the left side of subtree
        self.inordertraversal(root.left,currsum)
        #logic for adding currsum to result
        if root.left==None and root.right==None:
            self.result+=currsum
            
        
        #checking the right side of subtree
        self.inordertraversal(root.right,currsum)
        
        
        