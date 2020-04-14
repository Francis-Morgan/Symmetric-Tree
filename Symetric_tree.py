class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(left,right):
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False
            elif left.val != right.val:
                return False
            else:
                return check(left.left, right.right) and check(left.right,right.left)
          
        if root is None:
            return True
        return check(root.left,root.right)
        
       
       
  
    
    

 
            
