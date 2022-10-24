# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
       #ititializing the targetSum
        self.targetSum=targetSum
         #ititializing the result list array to store path 
        self.result=[]
        self.recur(root,0,[])
        #returning the result array list
        return self.result
    
    #defining the recur function whcih has currsum and path arguments which is changable at every iteration
    def recur(self,root,currsum,path):
    #base condition
        if root==None:
            return

        currsum=currsum+root.val
        path.append(root.val)

        #checking the left subtree of the node
        self.recur(root.left,currsum,path)

        #only when the left and right subtree is hitting null condition
        if root.left==None and root.right==None:
            #if the targetsum is equal to currsum append the roo.val to path list
            if currsum==self.targetSum:
                #we need to do a shallow copy
                temp=path[:]
                #appending it to the path list
                self.result.append(temp)


        #checking the right subtree of the node
        self.recur(root.right,currsum,path)
        #as it is pointer we need to pop it 
        path.pop()